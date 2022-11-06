import ast

from api.infrastructure.models import Data
from django.http import Http404
from rest_framework.request import HttpRequest

from .domain.serializers.response_serializer import DataSerializer


class ApiService:
    
    def get_data(self, id: str):
        """Retrive the data if the id correspond with the id given
        params: id, the id passed in the endpoint
        """
        try:
            data = Data.objects.get(id_data=id)
            serializer = DataSerializer(data)
            return serializer.data
        except Data.DoesNotExist as e:
            raise Http404(e)
    
    def update_data(self, request: HttpRequest):
        """Update or create the data passed in the request
        params: request, the request passed in the endpoint
        """
        serializer = DataSerializer(data=ast.literal_eval(str(request.data).lower()))
        if serializer.is_valid(raise_exception=True):
            if Data.objects.filter(id_data=request.data['ID']).exists():
                Data.objects.filter(id_data=request.data['ID']).update(**serializer.data)
            else:
                serializer.save()

    def update_single_record(self, request: HttpRequest, id: str):
        """Update the data matching the records in the database
            params: request, the request passed in the endpoint
                    id, the id passed in the endpoint
        """
        try:
            Data.objects.get(id_data=id)
            serializer = DataSerializer(data=ast.literal_eval(str(request.data).lower()))
            if serializer.is_valid():
                Data.objects.filter(id_data=id).update(**serializer.data)
        except Data.DoesNotExist as e:
            raise Http404(e)
    
    def delete_data(self, id: str):
        """delete the record with the corrispondent id
            params: id, the id passed in the endpoint
        """
        try:
            instance = Data.objects.get(id_data=id)
            instance.delete()
        except Data.DoesNotExist as e:
            raise Http404(e)
