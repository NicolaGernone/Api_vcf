import datetime
import json
import unittest

from api.application.api_service import ApiService
from api.infrastructure.models import Data
from api.infrastructure.views import ApiClient
from django.contrib.auth.models import User
from django.http import HttpRequest
from django.test import Client, TestCase
from model_bakery import baker
from rest_framework import status
from rest_framework.test import APIRequestFactory, force_authenticate


class ApiViewTest(TestCase):
    
    unittest.TestCase.maxDiff = None

    def setUp(self) -> None:
        self.api_service = ApiService()
        self.api_view = ApiClient(self.api_service)
        self.user = User.objects.create_user(username='tester', password='test1234', email='test@example.com')
        self.user.save()
        self.client = Client()
        self.client.login(username='tester', password='test1234')
        self.factory = APIRequestFactory()
        

    def test_post_ok(self) -> None:
        request = self.factory.post('/data/update/', {"CHROM": "chr1", "POS": 1000, "ALT": "A", "REF": "G", "ID": "rs123"})
        request.user = self.user
        force_authenticate(request, user=self.user, token=self.user.auth_token)
        self.assertEqual(request.status_code, status.HTTP_200_OK)

    def test_post_fail(self) -> None:
        request = self.factory.post('/data/update/', {"CHROM": "chr1", "POS": 1000, "ALT": "A", "REF": "G", "ID": "rs123"})
        request.user = self.user
        force_authenticate(request, user=self.user, token=self.user.auth_token)
        self.assertEqual(request.status_code, status.HTTP_404_NOT_FOUND)

    def test_post_no_auth(self) -> None:
        request = self.factory.post('/data/update/', {"CHROM": "chr1", "POS": 1000, "ALT": "A", "REF": "G", "ID": "rs123"})
        request.user = self.user
        force_authenticate(request, user=self.user, token=self.user.auth_token)
        self.assertEqual(request.status_code, status.HTTP_403_FORBIDDEN)

    def test_get_ok(self) -> None:
        request = self.factory.post('/data/update/', {"CHROM": "chr1", "POS": 1000, "ALT": "A", "REF": "G", "ID": "rs123"})
        request.user = self.user
        force_authenticate(request, user=self.user, token=self.user.auth_token)
        self.assertEqual(request.status_code, status.HTTP_200_OK)

    def test_get_fail(self) -> None:
        request = self.factory.post('/data/update/', {"CHROM": "chr1", "POS": 1000, "ALT": "A", "REF": "G", "ID": "rs123"})
        request.user = self.user
        force_authenticate(request, user=self.user, token=self.user.auth_token)
        self.assertEqual(request.status_code, status.HTTP_200_OK)

    def test_get_no_auth(self) -> None:
        request = self.factory.post('/data/update/', {"CHROM": "chr1", "POS": 1000, "ALT": "A", "REF": "G", "ID": "rs123"})
        request.user = self.user
        force_authenticate(request, user=self.user, token=self.user.auth_token)
        self.assertEqual(request.status_code, status.HTTP_403_FORBIDDEN)

    def test_get_headers_error(self) -> None:
        request = self.factory.post('/data/update/', {"CHROM": "chr1", "POS": 1000, "ALT": "A", "REF": "G", "ID": "rs123"})
        request.user = self.user
        force_authenticate(request, user=self.user, token=self.user.auth_token)
        self.assertEqual(request.status_code, status.HTTP_406_NOT_ACCEPTABLE)

    def test_put_ok(self) -> None:
        request = self.factory.post('/data/update/', {"CHROM": "chr1", "POS": 1000, "ALT": "A", "REF": "G", "ID": "rs123"})
        request.user = self.user
        force_authenticate(request, user=self.user, token=self.user.auth_token)
        self.assertEqual(request.status_code, status.HTTP_200_OK)

    def test_put_fail(self) -> None:
        request = self.factory.post('/data/update/', {"CHROM": "chr1", "POS": 1000, "ALT": "A", "REF": "G", "ID": "rs123"})
        request.user = self.user
        force_authenticate(request, user=self.user, token=self.user.auth_token)
        self.assertEqual(request.status_code, status.HTTP_200_OK)

    def test_put_no_auth(self) -> None:
        request = self.factory.post('/data/update/', {"CHROM": "chr1", "POS": 1000, "ALT": "A", "REF": "G", "ID": "rs123"})
        request.user = self.user
        force_authenticate(request, user=self.user, token=self.user.auth_token)
        self.assertEqual(request.status_code, status.HTTP_403_FORBIDDEN)

    def test_delete_ok(self) -> None:
        request = self.factory.post('/data/update/', {"CHROM": "chr1", "POS": 1000, "ALT": "A", "REF": "G", "ID": "rs123"})
        request.user = self.user
        force_authenticate(request, user=self.user, token=self.user.auth_token)
        self.assertEqual(request.status_code, status.HTTP_200_OK)

    def test_delete_fail(self) -> None:
        request = self.factory.post('/data/update/', {"CHROM": "chr1", "POS": 1000, "ALT": "A", "REF": "G", "ID": "rs123"})
        request.user = self.user
        force_authenticate(request, user=self.user, token=self.user.auth_token)
        self.assertEqual(request.status_code, status.HTTP_200_OK)

    def test_delete_no_auth(self) -> None:
        request = self.factory.post('/data/update/', {"CHROM": "chr1", "POS": 1000, "ALT": "A", "REF": "G", "ID": "rs123"})
        request.user = self.user
        force_authenticate(request, user=self.user, token=self.user.auth_token)
        self.assertEqual(request.status_code, status.HTTP_403_FORBIDDEN)