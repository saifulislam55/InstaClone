from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from . import views



urlpatterns = [
    path('<str:username>/post/<int:pk>/', views.post_detail, name='post_detail'),
    path('<str:username>/post_edit/<int:pk>/', views.post_edit, name='post_edit'),
    path('like/', views.like_toggle, name='like_toggle'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
