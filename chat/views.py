from django.contrib.auth.decorators import login_required
from .models import Message
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.utils.safestring import mark_safe
import json

from chat.forms import SignUpForm


@login_required
def index(request):
    return render(request, 'chat/index.html', {})


def logout(request):
    return render((request, 'accounts/logout.html', {}))


@login_required
def room(request, room_name):
    messages = Message.objects.all()
    return render(request, 'chat/room.html', {
        'room_name_json': mark_safe(json.dumps(room_name)),
        'username': mark_safe(json.dumps(request.user.username)),
        'messages': messages,
    })


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.birth_date = form.cleaned_data.get('birth_date')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})
