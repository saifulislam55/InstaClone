from django.urls import path
from . import views

urlpatterns = [
    path('notifications/', views.notifications, name='notifications'),
    path('notifications/read/<int:notif_id>/', views.mark_notification_as_read, name='mark_notification_as_read'),
]
