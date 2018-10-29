from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.utils.safestring import mark_safe
from .models import Chat,Room
from .forms import roomForm
import json

from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# 채팅방 리스트
@login_required
def index(request):
    print(request.user)
    users = User.objects.all()
    return render(request,'chat/index.html',{'users':users})

def room(request, room_name):
    room = Room.objects.get(id=room_name)
    chats = Chat.objects.filter(room=room)
    return render(request, 'chat/room.html', {
        'room_name_json': mark_safe(json.dumps(room_name)),'chats' : chats
    })
