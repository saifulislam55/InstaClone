from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Reels(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    caption = models.CharField(max_length=500, )
    reel_file = models.FileField(upload_to='reels_file')
    like = models.ManyToManyField(User, related_name='liked_reel')
    


class Comment(models.Model):
    reel = models.ForeignKey(Reels, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=500, null=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Share(models.Model):
    reel = models.ForeignKey(Reels, on_delete=models.CASCADE, related_name='shares')
    user = models.ForeignKey(Reels, on_delete=models.CASCADE, related_name='shared_reels')
    created_at = models.DateTimeField(auto_now_add=True)