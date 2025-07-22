# Create your views here.

from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import CustomUserCreationForm  
from postsapp.models import PostUpload
from django.contrib.auth.models import User

def signup(request):
    if request.user.is_authenticated:
        return redirect('home')  
     
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')
    else:
        form = CustomUserCreationForm()

    context = {
        'form': form
    }
    return render(request, 'accounts/singup.html', context)





def logout_view(request):
    logout(request)
    return redirect('login')

from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User


def profile(request, username):
    profile_user = get_object_or_404(User, username=username)
    user_form = UserForm(instance=request.user)
    profile_form = ProfileForm(instance=request.user.profile)
    post_print = PostUpload.objects.filter(user=profile_user)
    post_html = PostUpload.objects.all()
 

    context = {
        'user_form': user_form,
        'profile_form': profile_form,
        'profile_user':profile_user,
        'post_print':post_print,
        'post_html':post_html,

    }

    return render(request, 'profile.html', context)


from . forms import ProfileForm, UserForm


def profile_edit(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():  # <-- Fix here
            user_form.save()
            profile_form.save()
            return redirect('profile', username=request.user.username)



    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)

    context = {
        'user_form': user_form,
        'profile_form': profile_form
    }

    return render(request, 'profile_edit.html', context)

# views.py
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Profile

@login_required
def toggle_follow(request, username):
    target_user = get_object_or_404(User, username=username)
    target_profile = target_user.profile
    current_profile = request.user.profile

    if request.user in target_profile.followers.all():
        # Unfollow
        target_profile.followers.remove(request.user)
        current_profile.following.remove(target_user)
    else:
        # Follow
        target_profile.followers.add(request.user)
        current_profile.following.add(target_user)

    return redirect('profile', username=username)

