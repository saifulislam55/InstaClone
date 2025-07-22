from django.urls import path
from . import views

urlpatterns = [
    path('message/', views.message_list, name='message_list'),
    path('chat/<str:username>/', views.chat_view, name='chat_view'),
]
