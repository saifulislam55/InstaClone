from django.db import models
from django.contrib.auth.models import User

class PostUpload(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # many posts per user
    caption = models.CharField(max_length=100)
    post_file = models.FileField(upload_to='post_files/')  # Folder in MEDIA_ROOT
    created_at = models.DateTimeField(auto_now_add=True)    # Fixed field name
    updated_at = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(User, related_name='liked_posts', blank=True)
    unlike = models.ManyToManyField(User, related_name='unlike', blank= True)

    def __str__(self):
        return f"{self.user.username} - {self.caption}"
