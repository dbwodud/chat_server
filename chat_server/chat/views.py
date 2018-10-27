from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.utils.safestring import mark_safe
from .models import Chat,Room
from .forms import roomForm
import json

# 채팅방 메인 화면

def index(request):
    if request.method == 'POST':
        form = roomForm(request.POST)
        if form.is_valid():
            room_name = form.cleaned_data['room_name']
            Room(room_name=room_name).save() #채팅
            room_id = Room.objects.last().id
            return HttpResponseRedirect(str(room_id))
    else:
        form = roomForm()
        rooms = Room.objects.all()

    return render(request,'chat/index.html',{'form':form,'rooms':rooms})

def room(request, room_name):
    room = Room.objects.get(id=room_name)
    chats = Chat.objects.filter(room=room)
    for chat in chats:
        print(chat.chat)
    return render(request, 'chat/room.html', {
        'room_name_json': mark_safe(json.dumps(room_name)),'chats' : chats
    })
