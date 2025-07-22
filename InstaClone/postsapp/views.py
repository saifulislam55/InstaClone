from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from .models import PostUpload
from accounts.models import Profile
from postsapp.forms import PostUploadForm

def post_detail(request, username, pk):
    user = get_object_or_404(User, username=username)
    post = get_object_or_404(PostUpload, pk=pk, user=user)
    profile = get_object_or_404(Profile, user__username=username)
    return render(request, 'post.html', {'post': post , 'profile': profile})

from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User

def post_edit(request, username, pk):

    user =get_object_or_404(User, username=username)
    post = get_object_or_404(PostUpload, pk=pk, user=user)
    
    if request.method == 'POST':
        form = PostUploadForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail', username=username, pk=pk)
        
    else:
        form = PostUploadForm(instance=post)    

    return render(request, 'post_edit.html', {'form': form})

@login_required(login_url='login')  # Redirect to login page if not logged in
def like_toggle(request):
    post_id = request.GET.get('post_id')
    post = get_object_or_404(PostUpload, id=post_id)

    if request.user in post.likes.all():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)

    return redirect(request.META.get('HTTP_REFERER', '/'))


from rest_framework import viewsets,permissions
from .serializers import PostUploadSerializer


class PostUploadViewSet(viewsets.ModelViewSet):
    queryset = PostUpload.objects.all()
    serializer_class = PostUploadSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]