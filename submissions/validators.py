from django.utils import timezone
from rest_framework import serializers
from rest_framework.exceptions import NotFound

from hackathon.models import Hackathon


def validate_submission(attrs, hackathon, user):
    # validate a submission is submitted
    submission_types = [attrs.get('link'), attrs.get('file'), attrs.get('image')]
    submission_type = hackathon.submission_type

    if not any(submission_types):
        raise serializers.ValidationError(f'Submission of {submission_type} is required')
    
    # Check if hackathon has started
    if hackathon.start_datetime < timezone.now():
        raise serializers.ValidationError('Hackathon has already started. Submissions cannot be accepted or edited.')

    # validate participant submission matches hackathon submission type
    if submission_type == 'image' and not attrs.get('image'):
        raise serializers.ValidationError('Image submission is required.')

    if submission_type == 'file' and not attrs.get('file'):
        raise serializers.ValidationError('File submission is required.')

    if submission_type == 'link' and not attrs.get('link'):
        raise serializers.ValidationError('Link submission is required.')
    
    # validate user is a hackathon participant
    if user not in hackathon.participants.all():
        raise serializers.ValidationError(f'You have to enroll to {hackathon.title} before you can make a submission.')


def validate_hackathon(self, attrs):
    request = self.context.get('request')
    hackathon_id= request.data.get('hackathon_id')
    user = request.user

    try:
        hackathon = Hackathon.objects.get(id=hackathon_id)
    except Hackathon.DoesNotExist:
        raise NotFound('Hackathon not found')

    # call validate submission
    validate_submission(attrs, hackathon, user)

    return attrs
