from django.urls import path

from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

# contains all hackathon list('hackathon/') and detail(hackathon/<int:pk>/) endpoints
router.register('', views.HackathonViewset, basename='hackathon')

urlpatterns = [
    path('<int:id>/register/', views.HackathonRegistrationView.as_view(),name='hackathon-registration'),
    path('enrolled/', views.EnrolledHackthonListView.as_view(),name='hackathon-enrolled'),
]

urlpatterns += router.urls