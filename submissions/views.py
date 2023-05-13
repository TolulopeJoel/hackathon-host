from rest_framework import viewsets
from rest_framework.exceptions import NotFound

from hackathon.models import Hackathon

from .models import Submission
from .serializers import SubmissionSerializer


class SubmissionsViewset(viewsets.ModelViewSet):
    queryset = Submission.objects.all()
    serializer_class = SubmissionSerializer
    
    def get_queryset(self):
        user = self.request.user
        queryset = super().get_queryset()
        
        return queryset.filter(user=user)

    def perform_create(self, serializer):
        hackathon_id = self.request.data.get('hackathon_id')
        try:
            hackathon = Hackathon.objects.get(pk=hackathon_id)
        except Hackathon.DoesNotExist:
            raise NotFound('Hackathon not found')
        serializer.save(user=self.request.user, hackathon=hackathon)

