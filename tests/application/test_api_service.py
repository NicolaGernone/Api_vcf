from api.application.api_service import ApiService
from api.application.domain.serializers.response_serializer import \
    DataSerializer
from api.infrastructure.models import Data
from django.http import Http404
from django.test import TestCase
from model_bakery import baker
from rest_framework.request import HttpRequest
from rest_framework.exceptions import ValidationError


class ApiServiceTest(TestCase):

    def setUp(self):
        self.api_service = ApiService()
        self.request = HttpRequest()
        self.request.data = {"CHROM": "chr1", "POS": 1000, "ALT": "A", "REF": "G", "ID": "rs12345"}

    def test_get_data_ok(self):
        data = baker.make(Data, id_data='rs12345')
        response = self.api_service.get_data(id='rs12345')
        dataSet = DataSerializer(data)
        self.assertEqual(response, dataSet.data)

    def test_get_data_fail(self):
        baker.make(Data, id_data='rs1')
        with self.assertRaises(Http404):
            self.api_service.get_data(id='rs12345')

    def test_update_data_ok(self):
        baker.make(Data, id_data='rs12345')
        response = self.api_service.update_data(self.request)
        self.assertEqual(response, None)

    def test_update_data_fail(self):
        self.request.data = {}
        with self.assertRaises(ValidationError):
            self.api_service.update_data(self.request)

    def test_delete_data_ok(self):
        baker.make(Data, id_data='rs12345')
        response = self.api_service.delete_data(id='rs12345')
        self.assertEqual(response, None)

    def test_delete_data_fail(self):
        baker.make(Data, id_data='rs1')
        with self.assertRaises(Http404):
            self.api_service.delete_data(id='rs12345')

    def test_update_single_data_ok(self):
        baker.make(Data, id_data='rs12345')
        response = self.api_service.update_single_record(id='rs12345', request=self.request)
        self.assertEqual(response, None)

    def test_update_single_data_fail(self):
        self.request.data = {}
        with self.assertRaises(Http404):
            self.api_service.update_single_record(id='rs12345', request=self.request)
