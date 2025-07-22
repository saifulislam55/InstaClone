from django.shortcuts import render, get_object_or_404
from postsapp.models import PostUpload

# Create your views here.



def explore(request):
    posts = PostUpload.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'explore.html', context)
