from django.shortcuts import render
from accounts.models import Profile
from postsapp.models import PostUpload
from django.db.models import Q

# Create your views here.

def search(request):
    keyword = request.GET.get('keyword', '')

    users = Profile.objects.filter(Q(user__username__icontains=keyword)).select_related('user')

    posts = PostUpload.objects.filter(Q(caption__icontains=keyword)).prefetch_related('user')

    context = {
        'keyword': keyword,
        'users': users,
        'posts': posts,
    }

    return render(request, 'search.html', context)