from api.infrastructure.models import Data
from .domain.serializers.response_serializer import DataSerializer

class ApiService:
    
    def get_data(self, id):
        try:
            data = Data.objects.get(id_data=id)
            serializer = DataSerializer(data)
            return serializer
        except Data.DoesNotExist as e:
            raise Data.DoesNotExist(e)
    
    def update_data(self, request):
        try:
            serializer = DataSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                Data.objects.update_or_create(Data, get_fields=serializer.fields)
        except Data.DoesNotExist as e:
            raise Data.DoesNotExist(e)

    def update_single_record(self, request, id):
        try:
            record = Data.objects.get(id_data=id)
            serializer = DataSerializer(record, data=request.data)
            if serializer.is_valid():
                serializer.save()
                Data.objects.update_or_create(Data, get_fields=serializer.fields)
        except Data.DoesNotExist as e:
            raise Data.DoesNotExist(e)
    
    def delete_data(self, id):
        try:
            instance = Data.objects.get(id_data=id)
            instance.delete()
        except Data.DoesNotExist as e:
            raise Data.DoesNotExist(e)