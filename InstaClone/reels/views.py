from django.shortcuts import render, redirect, get_object_or_404
from .forms import ReelUploadForm,CommentForm
from .models import Reels

def reels(request):
    reels = Reels.objects.all()

    context = {
        'reels': reels
    }
    return render(request, 'reels.html', context)



def reel_upload(request):
    if request.method == 'POST':
        form = ReelUploadForm(request.POST, request.FILES)
        if form.is_valid():
            reel = form.save(commit=False)
            reel.user = request.user
            reel.save()
            return redirect('home')
    else:
        form = ReelUploadForm()

    context = {'form': form}
    return render(request, 'reel_upload.html', context)

def like_reel(request, reel_id):
    reel = get_object_or_404(Reels, id=reel_id)
    if request.user in reel.like.all():
        reel.like.remove(request.user)
    else:
        reel.like.add(request.user)
    return redirect('reels')




from .serializers import ReelsSerializers
from rest_framework import viewsets,permissions



class ReelsViewSet(viewsets.ModelViewSet):
    queryset = Reels.objects.all()
    serializer_class = ReelsSerializers
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]