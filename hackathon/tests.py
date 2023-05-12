from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model

from .models import Hackathon


class HackathonRegistrationViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

        # Create a test user
        self.user = get_user_model().objects.create_user(
            username='testuser',
            password='testpass'
        )

        # Create a test hackathon
        self.hackathon = Hackathon.objects.create(
            title='Test Hackathon',
            description='A test hackathon',
            background_image='background',
            hackathon_image='hackathon_image',
            sumbission_type='Image',
            start_datetime='2023-05-15:00:00:00',
            end_datetime='2023-05-16:00:00:00',
            reward_prize=300,
            organizer=self.user
        )

    def test_register_for_hackathon(self):
        """
        Test that a user can successfully register for a hackathon.
        """
        url = reverse('hackathon-registration')
        data = {'hackathon_id': self.hackathon.id}

        self.client.force_authenticate(user=self.user)
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(self.user in self.hackathon.participants.all())

    def test_already_registered(self):
        """
        Test that a user cannot register for a hackathon they are already registered for.
        """
        # Add the test user to the hackathon's participants
        self.hackathon.participants.add(self.user)

        url = reverse('hackathon-registration')
        data = {'hackathon_id': self.hackathon.id}

        self.client.force_authenticate(user=self.user)
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        # Check that the response message indicates the user is already registered
        self.assertEqual(response.data['message'], f'You are already registered for {self.hackathon.title}.')

    def test_hackathon_not_found(self):
        """
        Test that an error message is returned when trying to register for a hackathon that does not exist.
        """
        url = reverse('hackathon-registration')
        data = {'hackathon_id': 999}  # Invalid hackathon ID

        self.client.force_authenticate(user=self.user)
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data['detail'], 'Hackathon not found')

