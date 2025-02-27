from rest_framework.test import APITestCase, APIClient
from django.urls import reverse
from rest_framework import status

class LikeTest(APITestCase):
    
    def setUp(self):
        self.client = APIClient()

    def test_like_list(self):
        url = reverse('like-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code , status.HTTP_200_OK)