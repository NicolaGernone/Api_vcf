from api.application.api_service import ApiService
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class ApiClient(APIView):
    """
    Retrieve, update or delete istances.
    """
    def __init__(self, api_service=ApiService()):
        self.service = api_service

    def post(self, request) -> Response:
        return Response(self.service.update_data(request), status=status.HTTP_201_CREATED)

    def get(self, request, id) -> Response:
        return Response(self.service.get_data(id), status=status.HTTP_200_OK)

    def put(self, request, id) -> Response:
        return Response(self.service.update_single_record(request=request, id=id), status=status.HTTP_200_OK)

    def delete(self, request, id) -> Response:
        return Response(self.service.delete_data(id), status=status.HTTP_204_NO_CONTENT)
