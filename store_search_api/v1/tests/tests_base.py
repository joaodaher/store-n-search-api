from django.utils import timezone
from rest_framework.test import APITransactionTestCase

from v1 import models
from v1.tasks import create_event_mapping


class FieldFactoryMixin:
    def make_event(self, **kwargs):
        fields = {
            'name': 'buy',
            'timestamp': timezone.now(),
        }
        fields.update(**kwargs)
        return fields


class ModelFactoryMixin(FieldFactoryMixin):
    def save_event(self, **kwargs):
        fields = super().make_event(**kwargs)
        model = models.Event.objects.create(**fields)
        return fields, model


class BaseViewTest(ModelFactoryMixin, APITransactionTestCase):
    def tearDown(self):
        create_event_mapping()

    def assertIdInResponse(self, members, response):
        data = response.data
        try:
            results = data['results']
        except KeyError:
            results = [data]
        ids = [r.get('id') for r in results]

        if not isinstance(members, list):
            members = [members]
        for member in members:
            _id = member.get('id')
            self.assertIn(_id, ids)
            ids.remove(_id)
        self.assertEqual(any(ids), False)
