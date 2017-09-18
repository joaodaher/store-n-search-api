from rest_framework import status

from v1 import models
from v1.tests.tests_base import BaseViewTest


class SampleViewTests(BaseViewTest):
    url = '/v1/samples'

    def test_list_sample(self):
        sample_1, _ = self.save_sample(id=1)
        sample_2, _ = self.save_sample(id=2)

        url = self.url
        response = self.client.get(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIdInResponse([sample_1, sample_2], response)

    def test_detail_sample(self):
        provider_1, _ = self.save_sample(id=1)

        url = '{}/{}'.format(self.url, 1)
        response = self.client.get(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIdInResponse(provider_1, response)

    def test_post_sample(self):
        data = self.make_sample(id=1)
        url = self.url
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(models.Sample.objects.count(), 1)
