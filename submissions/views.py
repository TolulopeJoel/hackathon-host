from rest_framework import viewsets

from .models import Submission
from .serializers import SubmissionSerializer


class SubmissionsViewset(viewsets.ModelViewSet):
    queryset = Submission.objects.all()
    serializer_class = SubmissionSerializer
    
    def get_queryset(self):
        user = self.request.user
        queryset = super().get_queryset()
        
        return queryset.filter(user=user)


