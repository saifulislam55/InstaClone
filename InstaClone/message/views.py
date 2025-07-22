from django.shortcuts import render, get_object_or_404, redirect
from .models import Message
from .forms import MessageForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from accounts.models import Profile

# Create your views here.

@login_required
def message_list(request):
    users = User.objects.exclude(id=request.user.id)
    messages = Message.objects.filter(receiver=request.user).order_by('-timestamp')
    context = {
        
        'users': users, 
        'messages': messages

    }
    return render(request, 'messages.html',  context)

from django.db.models import Q

@login_required
def chat_view(request, username):
    receiver = get_object_or_404(User, username=username)
    profile = get_object_or_404(Profile, user__username=username)


    # Get all messages between the two users (2-way chat)
    messages = Message.objects.filter(
        Q(sender=request.user, receiver=receiver) |
        Q(sender=receiver, receiver=request.user)
    ).order_by('timestamp')

    # Mark unread messages as read
    messages.filter(receiver=request.user, is_read=False).update(is_read=True)

    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user
            message.receiver = receiver  # send to the other user
            message.save()
            return redirect('chat_view', username=receiver.username)
    else:
        form = MessageForm()

    context = {
        'messages': messages,
        'form': form,
        'receiver': receiver,
        'profile': profile

    }
    return render(request, 'chat.html', context)
