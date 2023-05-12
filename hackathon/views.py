from rest_framework import generics, viewsets
from rest_framework.exceptions import NotFound
from rest_framework.views import Response, status

from .models import Hackathon
from .serializers import HackathonSerializer


class HackathonViewset(viewsets.ModelViewSet):
    queryset = Hackathon.objects.all()
    serializer_class = HackathonSerializer
    
    def perform_create(self, serializer):
        organizer = self.request.user
        return serializer.save(organizer=organizer)


class HackathonRegistrationView(generics.CreateAPIView):
    queryset = Hackathon.objects.all()
    serializer_class = HackathonSerializer

    def get_object(self):
        hackathon_id = self.request.data.get('hackathon_id')
        try:
            return self.queryset.get(id=hackathon_id)
        except Hackathon.DoesNotExist:
            raise NotFound('Hackathon not found')

    def create(self, request, *args, **kwargs):
        """
        Add users as participants Hackathon
        """
        hackathon = self.get_object()
        user = request.user

        if user in hackathon.participants.all():
            response_data = {
                'message': f'You are already registered for {hackathon.title}.'
            }
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)

        try:
            hackathon.participants.add(user)
        except Exception as e:
            response_data = {
                'message': f'An error occurred while registering you for {hackathon.title}.'
            }
            return Response(response_data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        self.get_serializer(instance=hackathon)
        response_data = {
            'message': f'You have successfully registered for {hackathon.title}.'
        }
        return Response(response_data, status=status.HTTP_201_CREATED)

