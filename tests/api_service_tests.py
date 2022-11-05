import datetime
import json
from django.db import DatabaseError

from api.application.api_service import ApiService
from api.infrastructure.models import Data
from django.contrib.auth.models import User
from django.test import Client, TestCase
from model_bakery import baker


class ApiServiceTest(TestCase):

    def setUp(self):
        self.api_service = ApiService()
        self.user = User.objects.create_user(username='tester', password='test1234', email='test@example.com')
        self.user.save()
        self.client = Client()
        self.client.login(username='tester', password='test1234')

    def test_get_data_ok(self):
        self.data = baker.make(Data, _quantity=3)

        self.list_of_images = [
            {"id": self.images[0].id, "name": self.images[0].name, "weight": None, "url": self.images[0].url, "categories": None, "events": { "view": None, "click": None}},
            {"id": self.images[1].id, "name": self.images[1].name, "weight": None, "url": self.images[1].url, "categories": None, "events": { "view": None, "click": None}},
            {"id": self.images[2].id, "name": self.images[2].name, "weight": None, "url": self.images[2].url, "categories": None, "events": { "view": None, "click": None}}
            ]

        dataSet = {'data': self.list_of_images}
        request = self.request
        request.user = self.user
        response = self.api_service.get_images(request)
        self.assertEqual(response, dataSet)

    def test_get_data_fail(self):
        self.images = baker.make(Image, _quantity=3)
        self.event = baker.make(Event, image_id=self.images[0].id)

        self.list_of_images = [
            {"id": self.images[0].id, "name": self.images[0].name, "weight": None, "url": self.images[0].url, "categories": None, "events": { "view": None, "click": None}},
            {"id": self.images[1].id, "name": self.images[1].name, "weight": None, "url": self.images[1].url, "categories": None, "events": { "view": None, "click": None}},
            {"id": self.images[2].id, "name": self.images[2].name, "weight": None, "url": self.images[2].url, "categories": None, "events": { "view": None, "click": None}}
            ]

        dataSet = {'data': self.list_of_images}
        request = self.request
        request.user = self.user
        response = self.api_service.get_images(request)
        self.assertEqual(response, dataSet)

    def test_update_data_ok(self):
        image = baker.make(Image)
        request = self.request
        request.user = self.user
        body = bytes(json.dumps({"eventType": "click", "timestamp": datetime.datetime.now().timestamp()}), encoding='utf-8')
        request._body = body
        imageId = image.id
        response = self.api_service.set_events(request=request, imageId=imageId)
        self.assertEqual(response, {})

    def test_update_data_fail(self):
        image = baker.make(Image)
        request = self.request
        request.user = self.user
        body = bytes(json.dumps({"eventType": "click", "timestamp": datetime.datetime.now().timestamp()}), encoding='utf-8')
        request._body = body
        imageId = image.id
        response = self.api_service.set_events(request=request, imageId=imageId)
        self.assertEqual(response, {})

    def test_delete_data_ok(self):

        request = self.request
        request.user = self.user
        with self.assertRaises(DatabaseError):
            self.api_service.get_images(request)

    def test_delete_data_fail(self):

        request = self.request
        request.user = self.user
        with self.assertRaises(DatabaseError):
            self.api_service.get_images(request)

    def test_update_single_data_fail(self):
        request = self.request
        request.user = self.user
        body = bytes(json.dumps({ "eventType": "click", "timestamp": datetime.datetime.now().timestamp()}), encoding='utf-8')
        request._body = body
        imageId = None
        with self.assertRaises(DatabaseError):
            self.api_service.set_events(request=request, imageId=imageId)

    def test_update_single_data_ok(self):
        request = self.request
        request.user = self.user
        body = bytes(json.dumps({ "eventType": "click", "timestamp": datetime.datetime.now().timestamp()}), encoding='utf-8')
        request._body = body
        imageId = None
        with self.assertRaises(DatabaseError):
            self.api_service.set_events(request=request, imageId=imageId)