from rest_framework import serializers
from rest_framework.exceptions import NotFound

from hackathon.models import Hackathon


def validate_submission(attrs, hackathon):
    # validate a submission is submitted
    submission_types = [attrs.get('link'), attrs.get('file'), attrs.get('image')]
    submission_type = hackathon.submission_type

    if not any(submission_types):
        raise serializers.ValidationError(f'Submission of {submission_type} is required')
    

    # validate participant submission matches hackathon submission type
    if submission_type == 'image' and not attrs.get('image'):
        raise serializers.ValidationError('Image submission is required.')

    if submission_type == 'file' and not attrs.get('file'):
        raise serializers.ValidationError('File submission is required.')

    if submission_type == 'link' and not attrs.get('link'):
        raise serializers.ValidationError('Link submission is required.')


def validate_hackathon(self, attrs):
    request = self.context.get('request')
    hackathon_id= request.data.get('hackathon_id')

    try:
        hackathon = Hackathon.objects.get(id=hackathon_id)
    except Hackathon.DoesNotExist:
        raise NotFound('Hackathon not found')

    # call validate submission
    validate_submission(attrs, hackathon)

    return attrs
