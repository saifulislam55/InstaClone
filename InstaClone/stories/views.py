

from django.shortcuts import render, redirect, get_object_or_404
from .forms import StoryForm
from .models import Story
from datetime import timedelta
from django.utils import timezone
from accounts.models import Profile

def story_upload(request):
    if request.method == 'POST':
        form = StoryForm(request.POST, request.FILES)
        if form.is_valid():
            story = form.save(commit=False)
            story.user = request.user
            story.save()
            return redirect('home')
    else:
        form = StoryForm()
    return render(request, 'story.html', {'form': form})

 





def view_story(request, story_id):
    story = get_object_or_404(Story, id=story_id)
    profile_image = Profile.objects.values_list('profile_image', flat=True)
    return render(request, 'view_story.html', {'story': story, 'profile_image':profile_image})
