from rest_framework import generics, viewsets
from rest_framework.exceptions import NotFound
from rest_framework.views import Response, status

from .models import Hackathon
from .serializers import HackathonSerializer


class HackathonViewset(viewsets.ModelViewSet):
    """
    API endpoint that allows CRUD operations on Hackathon objects.
    """

    queryset = Hackathon.objects.all()
    serializer_class = HackathonSerializer

    def perform_create(self, serializer):
        """
        Create a new Hackathon object with the current user as the organizer.
        """
        organizer = self.request.user
        return serializer.save(organizer=organizer)


class EnrolledHackthonListView(generics.ListAPIView):
    """
    API endpoint that lists Hackathons where the current user is enrolled.
    """

    serializer_class = HackathonSerializer

    def get_queryset(self):
        """
        Get a list of Hackathons where the current user is enrolled.
        Returns:
            QuerySet: A queryset containing Hackathons with the current user as participant.
        """
        user = self.request.user
        return Hackathon.objects.filter(participants=user)


class HackathonRegistrationView(generics.CreateAPIView):
    """
    API endpoint for registering users for a specific Hackathon.
    """

    queryset = Hackathon.objects.all()
    serializer_class = HackathonSerializer

    def get_object(self):
        """
        Get the Hackathon object based on the 'id' URL parameter.
        """
        hackathon_id = self.kwargs.get('id')
        try:
            return self.queryset.get(id=hackathon_id)
        except Hackathon.DoesNotExist:
            raise NotFound('Hackathon not found')

    def create(self, request, *args, **kwargs):
        """
        Register the current user for a specific Hackathon.
        Add user as a participant to the Hackathon.
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
