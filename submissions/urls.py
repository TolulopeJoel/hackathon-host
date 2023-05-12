from django.urls import path

from . import views

urlpatterns = [
    path('', views.SubmissionListView.as_view(),)
]