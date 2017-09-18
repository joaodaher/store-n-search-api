from rest_framework import status

from v1 import models
from v1.tests.tests_base import BaseViewTest


class EventViewTests(BaseViewTest):
    url = '/v1/events/'

    def test_list_event(self):
        event_1, _ = self.save_event(name='signup')
        event_2, _ = self.save_event(name='login')

        url = self.url
        response = self.client.get(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIdInResponse([event_1, event_2], response)

    def test_detail_sample(self):
        event_1, _ = self.save_event(name='signup')

        url = '{url}{pk}/'.format(url=self.url, pk=1)
        response = self.client.get(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIdInResponse(event_1, response)

    def test_post_sample(self):
        data = self.make_event(name='signup')
        url = self.url
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(models.Event.objects.count(), 1)
