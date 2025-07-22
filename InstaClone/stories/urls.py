from django.urls import path
from . import views

urlpatterns = [
    path('story/upload/', views.story_upload, name='story_upload'),  # Upload story
    path('story/<int:story_id>/', views.view_story, name='view_story'),  # View single story
]
