from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from postsapp.forms import PostUploadForm
from postsapp.models import PostUpload
from django.shortcuts import render, redirect, get_object_or_404
from stories.models  import Story
from stories.forms import StoryForm
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from datetime import timedelta
from accounts.models import Profile

def login_view(request):
    
    if request.user.is_authenticated:
        return redirect('home')  # Redirect to home if already logged in

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()  # Get the authenticated user
            login(request, user)  # Pass both the request and the user to the login function
            return redirect('home')  # Redirect to a home page after successful login

    else:
        form = AuthenticationForm()  # Empty form to show initially

    context = {
        'form': form
    }
    
    return render(request, 'accounts/login.html', context)

@login_required
def home(request):
    if request.method == 'POST':
        form = PostUploadForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('profile', username=request.user.username )
        else:
            print(form.errors)
    else:
        form = PostUploadForm()

    current_user = request.user
    following_profiles = Profile.objects.filter(followers=current_user)
    following_users = [profile.user for profile in following_profiles]
    posts = PostUpload.objects.filter(user__in=following_users).order_by('-created_at')
    following_users.append(current_user)
    
    if request.user.is_authenticated:
        recent_time = timezone.now() - timedelta(hours=24)
        stories = Story.objects.filter(created_at__gte=recent_time).order_by('-created_at')
    else:
        stories = []
        




    
    context = {
        'form': form,
        'posts': posts,
        'stories': stories,
    }

    return render(request, 'home_feed.html', context)  # ✅ NOT a new PostUploadForm()



