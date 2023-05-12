from rest_framework import serializers

from . import validators
from .models import Submission


class SubmissionSerializer(serializers.ModelSerializer):
    user = serializers.CharField(read_only=True)
    hackathon = serializers.CharField(read_only=True)

    class Meta:
        model = Submission
        fields = '__all__'

    def validate(self, attrs):
        attrs = super().validate(attrs)
        attrs = validators.validate_hackathon(self, attrs)
        return attrs