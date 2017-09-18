from rest_framework.test import APITransactionTestCase

from v1 import models


class FieldFactoryMixin:
    def make_sample(self, **kwargs):
        fields = {
            'name': 'My Sample',
        }
        fields.update(**kwargs)
        return fields


class ModelFactoryMixin(FieldFactoryMixin):
    def save_sample(self, **kwargs):
        fields = super().make_sample(**kwargs)
        model = models.Sample.objects.create(**fields)
        return fields, model


class BaseViewTest(ModelFactoryMixin, APITransactionTestCase):
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
