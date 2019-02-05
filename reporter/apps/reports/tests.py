from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User


# Create your tests here.
class ReportsTests(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(username='testuser', email='a@a.es', password='asdfqwer')

    def test_create_report(self):
        """Testing the creation of a report"""
        data = {
            'name': 'abcd',
            'reason': 'this is a test reason'
        }
        url = reverse('reports')
        response = self.client.post(url, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        self.client.force_login(user=self.user)

        url = reverse('reports')
        response = self.client.post(url, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
