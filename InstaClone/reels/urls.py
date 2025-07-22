from django.urls import path
from . import views

urlpatterns = [
    path('reels/', views.reels, name='reels'),
    path('reel_upload/', views.reel_upload, name='reel_upload'),
    path('like_reel/<int:reel_id>/', views.like_reel, name='like_reel'),
]
