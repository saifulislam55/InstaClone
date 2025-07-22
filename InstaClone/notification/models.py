# models.py
from django.db import models
from django.contrib.auth.models import User

class Notification(models.Model):
    NOTIF_TYPE = (
        ('follow', 'Follow'),
        ('like', 'Like'),
    )

    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_notifications')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
    notification_type = models.CharField(max_length=10, choices=NOTIF_TYPE)
    is_read = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    message = models.TextField(blank=True, null=True)  # Optional: for custom text

    def __str__(self):
        return f"{self.sender} {self.notification_type} -> {self.receiver}"
