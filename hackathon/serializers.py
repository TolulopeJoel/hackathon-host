from django.utils import timezone
from rest_framework import serializers

from accounts.serializers import PublicUserSerializer

from .models import Hackathon


class HackathonSerializer(serializers.ModelSerializer):
    organizer = PublicUserSerializer(read_only=True)
    participants = PublicUserSerializer(read_only=True, many=True)

    class Meta:
        model = Hackathon
        fields = '__all__'

    def validate(self, attrs):
        start_datetime = attrs.get('start_datetime')
        end_datetime = attrs.get('end_datetime')
        
        # validates dates are not in the past.
        if start_datetime and end_datetime:
            if start_datetime < timezone.now():
                raise serializers.ValidationError('Start datetime cannot be in the past.')

            if end_datetime < timezone.now():
                raise serializers.ValidationError('End datetime cannot be in the past.')

            # validates end_datetime always greater than start_datetime
            if start_datetime >= end_datetime:
                raise serializers.ValidationError('Start datetime must be earlier than end datetime.')

        return attrs


class PublicHackathonSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    organizer = PublicUserSerializer(read_only=True)
    title = serializers.CharField(read_only=True)
    description = serializers.CharField(read_only=True)
    start_datetime = serializers.DateTimeField(read_only=True)
    end_datetime = serializers.DateTimeField(read_only=True)
