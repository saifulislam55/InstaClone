from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta

class Story(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='stories/')
    caption = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def profile_image(self):
        return self.user.profile.profile_image.url if self.user.profile.profile_image else None

    def is_expired(self):
        return timezone.now() > self.created_at + timedelta(hours=24)

    def __str__(self):
        return f"{self.user.username}'s story"

class StoryView(models.Model):  # Optional: to track who saw the story
    story = models.ForeignKey(Story, on_delete=models.CASCADE, related_name='views')
    viewer = models.ForeignKey(User, on_delete=models.CASCADE)
    viewed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.viewer.username} saw {self.story.user.username}'s story"
