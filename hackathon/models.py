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
    start_datetime = models.DateTimeField()
    reward_prize = models.PositiveIntegerField()
    
    organizer = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='organized_hackathons')
    participants = models.ManyToManyField(get_user_model())
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return self.title
    
