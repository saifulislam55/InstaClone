from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Notification

@login_required
def notifications(request):
    notifs = request.user.notifications.all().order_by('-timestamp')
    return render(request, 'notifications.html', {'notifications': notifs})

@login_required
def mark_notification_as_read(request, notif_id):
    notif = get_object_or_404(Notification, id=notif_id, receiver=request.user)
    notif.is_read = True
    notif.save()
    return redirect('notifications')
