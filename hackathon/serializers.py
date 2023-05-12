from django.utils import timezone
from rest_framework import serializers

from .models import Hackathon


class HackathonSerializer(serializers.ModelSerializer):
    organizer = serializers.CharField(read_only=True)

    class Meta:
        model = Hackathon
        fields = '__all__'
