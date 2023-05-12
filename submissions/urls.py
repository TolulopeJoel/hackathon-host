from django.urls import path

from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

# contains all user's submissions list('submissions/') and detail(submissions/<int:pk>/) endpoints
router.register('', views.SubmissionsViewset, basename='submissions')

urlpatterns = router.urls