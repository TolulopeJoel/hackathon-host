from django.contrib.auth import get_user_model
from django.test import TestCase

from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken


class AuthenticationTests(APITestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser', email='test@example.com', password='testpassword'
        )

    def test_token_obtain(self):
        url = '/api/token/'
        data = {'username': 'testuser', 'password': 'testpassword'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)

    def test_token_refresh(self):
        refresh = RefreshToken.for_user(self.user)
        url = '/api/token/refresh/'
        data = {'refresh': str(refresh)}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)

    def test_auth_required(self):
        url = '/api/protected/'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_auth_success(self):
        url = '/api/protected/'
        token = str(RefreshToken.for_user(self.user).access_token)
        headers = {'Authorization': f'Bearer {token}'}
        response = self.client.get(url, format='json', **headers)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['username'], 'testuser')
