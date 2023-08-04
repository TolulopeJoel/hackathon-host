from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from hackathon.models import Hackathon

from .models import Submission


class SubmissionsViewsetTest(APITestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass'
        )

        # Create a test hackathon
        self.hackathon = Hackathon.objects.create(
            organizer_id=self.user.id,
            title='Test Hackathon',
            description='Test description',
            reward_prize=300,
            start_datetime='2029-06-01T00:00:00Z',
            end_datetime='2029-06-11T00:00:00Z'
        )
        # Create a test submission
        self.submission_data = {
            'name': 'Test Submission',
            'summary': 'Test description',
            'link': 'https://hackathon.test.com',
            'hackathon_id': self.hackathon.id,
        }
        self.client.force_authenticate(user=self.user)

    def register_for_hackathon(self):
        registration_url = reverse(
            'hackathon-registration',
            kwargs={'id': self.user.id}
        )
        self.client.post(registration_url, format='json')

    def test_unerroled_user_cant_create_submission(self):
        """
        Test user not registered(enrolled) to hackathon can't create a submission.
        """
        url = reverse('submission-list')
        response = self.client.post(url, self.submission_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            response.data['non_field_errors'][0],
            "You have to enroll to Test Hackathon before you can make a submission."
        )

    def test_enrolled_user_can_create_submission(self):
        """
        Test creating a new submission.
        """

        # enroll to hackathon so user can make submission
        self.register_for_hackathon()

        # Create submission
        url = reverse('submission-list')
        response = self.client.post(url, self.submission_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        submission = Submission.objects.get(pk=response.data['id'])
        self.assertEqual(submission.user, self.user)
        self.assertEqual(submission.hackathon, self.hackathon)

    def test_create_submission_invalid_hackathon_id(self):
        """
        Test creating a submission with an invalid hackathon_id.
        """
        url = reverse('submission-list')
        invalid_data = self.submission_data.copy()
        invalid_data['hackathon_id'] = 9999
        response = self.client.post(url, invalid_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_get_user_submissions(self):
        """Test retrieving submissions of the authenticated user."""
        Submission.objects.create(
            name='Submission 1',
            summary='Description 1',
            user=self.user,
            hackathon=self.hackathon
        )
        Submission.objects.create(
            name='Submission 2',
            summary='Description 2',
            user=self.user,
            hackathon=self.hackathon
        )
        url = reverse('submission-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_get_other_user_submissions(self):
        """
        Test that other users' submissions are not accessible.
        """
        # Create another user and their submissions
        other_user = User.objects.create_user(
            username='otheruser',
            password='otherpass'
        )
        Submission.objects.create(
            name='Other User Submission',
            summary='Other user description',
            user=other_user,
            hackathon=self.hackathon
        )

        url = reverse('submission-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Should only show submissions of the authenticated user
        self.assertEqual(len(response.data), 0)

    def test_get_single_submission(self):
        """
        Test retrieving a single submission.
        """
        submission = Submission.objects.create(
            name='Single Submission',
            summary='Single submission description',
            user=self.user,
            hackathon=self.hackathon

        )
        url = reverse('submission-detail', args=[submission.id])
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], submission.name)

    def test_get_nonexistent_submission(self):
        """
        Test retrieving a non-existent submission.
        """
        url = reverse('submission-detail', args=[9999])
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_submission(self):
        """
        Test updating a submission.
        """

        # enroll to hackathon so user can make submission
        self.register_for_hackathon()

        submission = Submission.objects.create(
            name='Old Title',
            summary='Old description',
            user=self.user,
            hackathon=self.hackathon
        )
        url = reverse('submission-detail', args=[submission.id])
        update_data = {
            'name': 'New Title',
            'summary': 'New description',
            'link': 'https://test.com/',
            'hackathon_id': self.hackathon.id,
        }
        response = self.client.put(url, update_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        submission.refresh_from_db()
        self.assertEqual(submission.name, 'New Title')
        self.assertEqual(submission.summary, 'New description')

    def test_update_submission_invalid_hackathon_id(self):
        """
        Test updating a submission with an invalid hackathon_id.
        """
        submission = Submission.objects.create(
            name='Old Title',
            summary='Old description',
            user=self.user,
            hackathon=self.hackathon
        )
        url = reverse('submission-detail', args=[submission.id])
        invalid_data = {
            'name': 'New Title',
            'summary': 'New description',
            'hackathon_id': 9999,  # Assuming there is no hackathon with this ID
        }
        response = self.client.put(url, invalid_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_delete_submission(self):
        """
        Test deleting a submission.
        """
        submission = Submission.objects.create(
            name='To be deleted',
            summary='Description to be deleted',
            user=self.user,
            hackathon=self.hackathon
        )
        url = reverse('submission-detail', args=[submission.id])
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Submission.objects.filter(pk=submission.id).exists())

    def test_delete_nonexistent_submission(self):
        """
        Test deleting a non-existent submission.
        """
        url = reverse('submission-detail', args=[9999])
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
