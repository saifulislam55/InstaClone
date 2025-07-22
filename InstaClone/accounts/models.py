from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(upload_to='profile_images/', default='profile_images/default.png')
    bio = models.TextField(max_length=100, blank=True)
    website = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    github = models.URLField(blank=True)
    followers = models.ManyToManyField(User,related_name='profile_followers', blank=True)
    following = models.ManyToManyField(User,related_name='profile_following', blank=True)


    def __str__(self):
        return f"{self.user.username}'s Profile"
    
    def followers_count(self):
        return self.followers.count()
    
    def following_count(self):
        return self.following.count()





