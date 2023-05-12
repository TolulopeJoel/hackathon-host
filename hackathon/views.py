from rest_framework import viewsets

from .models import Hackathon
from .serializers import HackathonSerializer


class HackathonViewset(viewsets.ModelViewSet):
    queryset = Hackathon.objects.all()
    serializer_class = HackathonSerializer
    
    def perform_create(self, serializer):
        organizer = self.request.user
        return serializer.save(organizer=organizer)
