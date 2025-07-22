from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),  # Direct to the accounts app URLs
    path('', views.login_view, name='login') ,
    path('home', views.home, name='home')  ,
    path('api/', include('postsapp.urls')),
    path('', include('stories.urls')),  
    path('', include('searchapp.urls')),  
    path('', include('explore.urls')),  
    path('', include('message.urls')),  
    path('', include('notification.urls')),  
    path('', include('reels.urls')),
    path('api/reels/', include('reels.api_urls')),
    path('api/posts/', include('postsapp.api_urls'))





]
