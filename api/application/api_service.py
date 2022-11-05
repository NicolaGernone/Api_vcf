import ast
from api.infrastructure.models import Data
from django.http import Http404
from .domain.serializers.response_serializer import DataSerializer

class ApiService:
    
    def get_data(self, id):
        try:
            data = Data.objects.get(id_data=id)
            serializer = DataSerializer(data)
            return serializer.data
        except Data.DoesNotExist as e:
            raise Http404(e)
    
    def update_data(self, request):
        try:
            serializer = DataSerializer(data=ast.literal_eval(str(request.data).lower()))
            if serializer.is_valid():
                if Data.objects.filter(id_data=request.data['ID_DATA']).exists():
                    Data.objects.filter(id_data=request.data['ID_DATA']).update(**serializer.data)
                else:
                    serializer.save()
        except Data.DoesNotExist as e:
            raise Http404(e)

    def update_single_record(self, request, id):
        try:
            Data.objects.get(id_data=id)
            serializer = DataSerializer(data=ast.literal_eval(str(request.data).lower()))
            if serializer.is_valid():
                Data.objects.filter(id_data=id).update(**serializer.data)
        except Data.DoesNotExist as e:
            raise Http404(e)
    
    def delete_data(self, id):
        try:
            instance = Data.objects.get(id_data=id)
            instance.delete()
        except Data.DoesNotExist as e:
            raise Http404(e)