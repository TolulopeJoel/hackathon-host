from django.db import models
from django.contrib.auth import get_user_model


class Hackathon(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    background_image = models.ImageField(upload_to='hackathon_backgrounds/')
    hackathon_image = models.ImageField(upload_to='hackathon_images/')
    SUBMISSION_TYPE_CHOICES = [
        ('image', 'Image'),
        ('file', 'File'),
        ('link', 'Link'),
    ]
    sumbission_type = models.CharField(max_length=10, choices=SUBMISSION_TYPE_CHOICES)
    end_datetime = models.DateTimeField()
    reward_prize = models.PositiveIntegerField()
    start_datetime = models.DateTimeField()
    
    organizer = models.ManyToManyField(get_user_model(), related_name='organized_hackathons')

    def __str__(self):
        return self.title
    
