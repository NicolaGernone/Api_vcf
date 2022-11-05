from api.application.api_service import ApiService
from django.http import Http404
from rest_framework import status
from rest_framework.authentication import (BasicAuthentication,
                                           SessionAuthentication)
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model


class ApiClient(APIView):
    """
    Retrieve, update or delete istances.
    """
    def __init__(self, api_service=ApiService()):
        self.service = api_service

    renderer_classes = (TemplateHTMLRenderer, JSONRenderer)
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        return Response(self.service.update_data(request=request), status=status.HTTP_201_CREATED)

    def get(self, request, id):
        if request.accepted_renderer.format == 'html' and request.accepted_renderer.format == 'json':
            return Response(self.service.get_data(id), status=status.HTTP_200_OK)
        else:
            Response(status=status.HTTP_406_NOT_ACCEPTABLE)

    def put(self, request, id):
        return Response(self.service.update_data(request=request, id=id), status=status.HTTP_200_OK)

    def delete(self, request, id):
        return Response(self.service.delete_data(id), status=status.HTTP_204_NO_CONTENT)
