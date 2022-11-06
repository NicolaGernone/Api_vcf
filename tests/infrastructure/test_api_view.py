import json
import unittest

from api.application.api_service import ApiService
from api.infrastructure.models import Data
from api.infrastructure.views import ApiClient
from django.contrib.auth.models import User
from model_bakery import baker
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient, APITestCase


class ApiViewTest(APITestCase):
    
    unittest.TestCase.maxDiff = None

    def setUp(self) -> None:
        self.api_service = ApiService()
        self.api_view = ApiClient(self.api_service)
        self.client = APIClient()
        User.objects.create(username='tester', password='Test91234#')
        user = User.objects.get(username='tester')
        Token.objects.create(user=user)
        self.token = Token.objects.get(user__username=user)
        self.client.login(username='tester', password='Test91234#')
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        

    def test_post_ok(self) -> None:
        data = baker.make(Data, id_data='rs12345')
        response = self.client.post('/data/update/', content_type='application/json', data=json.dumps({"CHROM": "chr1", "POS": 1000, "ALT": "A", "REF": "G", "ID": "rs12345"}))
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_post_fail(self) -> None:
        response = self.client.post('/data/update/', data=None)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_post_no_auth(self) -> None:
        data = baker.make(Data, id_data='rs12345')
        self.client.credentials()
        response = self.client.post('/data/update/', data=json.dumps({"CHROM": "chr1", "POS": 1000, "ALT": "A", "REF": "G", "ID": "rs12345"}), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_ok(self) -> None:
        data = baker.make(Data, id_data='rs12345')
        response = self.client.get('/data/rs12345')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_fail(self) -> None:
        data = baker.make(Data, id_data='rs12345')
        response = self.client.get('/data/x')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_get_no_auth(self) -> None:
        data = baker.make(Data, id_data='rs12345')
        self.client.credentials()
        response = self.client.get('/data/rs12345')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_headers_error(self) -> None:
        data = baker.make(Data, id_data='rs12345')
        header = {'HTTP_ACCEPT': 'text/html'}
        response = self.client.get('/data/rs12345', **header)
        self.assertEqual(response.status_code, status.HTTP_406_NOT_ACCEPTABLE)

    def test_put_ok(self) -> None:
        data = baker.make(Data, id_data='rs12345')
        response = self.client.put('/data/update/rs12345', content_type='application/json', data=json.dumps({"CHROM": "chr1", "POS": 1000, "ALT": "A", "REF": "G", "ID": "rs12345"}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_put_fail(self) -> None:
        data = baker.make(Data, id_data='rs12345')
        response = self.client.put('/data/update/rs', content_type='application/json', data=json.dumps({"CHROM": "chr1", "POS": 1000, "ALT": "A", "REF": "G", "ID": "rs12345"}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_put_no_auth(self) -> None:
        data = baker.make(Data, id_data='rs12345')
        self.client.credentials()
        response = self.client.put('/data/update/xd', content_type='application/json', data=json.dumps({"CHROM": "chr1", "POS": 1000, "ALT": "A", "REF": "G", "ID": "rs12345"}))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_delete_ok(self) -> None:
        data = baker.make(Data, id_data='rs12345')
        response = self.client.delete('/data/delete/rs12345')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_fail(self) -> None:
        data = baker.make(Data, id_data='rs12345')
        response = self.client.delete('/data/delete/xd')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_delete_no_auth(self) -> None:
        data = baker.make(Data, id_data='rs12345')
        self.client.credentials()
        response = self.client.delete('/data/delete/rs12345')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
