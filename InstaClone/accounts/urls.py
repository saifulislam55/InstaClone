# accounts/urls.py
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('signup/', views.signup, name='signup'),  # Signup view in the accounts app_
    path('logout/', views.logout_view , name='logout'),
    path('profile/<str:username>/', views.profile, name='profile'),
    path('profile_edit/', views.profile_edit , name='profile_edit' ),
    path('follow/<str:username>/', views.toggle_follow, name='toggle_follow'),

    

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)