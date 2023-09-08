from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import WorshipSchedule


class WorshipScheduleViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        # Replace this with the actual endpoint URL
        self.url = '/api/worship-info/'
        self.valid_payload = {
            'info': {
                'key1': 'value1',
                'key2': 'value2',
            }
        }

    def test_create_worship_schedule(self):
        # Test creating a new WorshipSchedule when none exists
        response = self.client.put(self.url, self.valid_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(WorshipSchedule.objects.count(), 1)
        self.assertEqual(WorshipSchedule.objects.first().info,
                         self.valid_payload['info'])

    def test_update_worship_schedule(self):
        # Create an initial WorshipSchedule object
        WorshipSchedule.objects.create(
            info={
                'key1': 'initial_value1',
                'key2': 'initial_value2',
            }
        )
        # Test updating the existing WorshipSchedule
        response = self.client.put(self.url, self.valid_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(WorshipSchedule.objects.count(),
                         1)  # Count should still be 1
        updated_worship_info = WorshipSchedule.objects.first()
        self.assertEqual(updated_worship_info.info, self.valid_payload['info'])

    # def test_invalid_payload(self):
    #     # Test with invalid payload
    #     invalid_payload = {
    #         'info': '',  # An empty string should be invalid for a JSONField
    #     }
    #     response = self.client.put(self.url, invalid_payload, format='json')
    #     self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
