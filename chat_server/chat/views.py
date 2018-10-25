from django.shortcuts import render
from django.utils.safestring import mark_safe
from .models import Chat,Room

import json

def index(request):
    #Room List
    rooms = Room.objects.all()
    return render(request, 'chat/index.html', {'rooms':rooms})

def room(request, room_name):
    # First crate room and The others just pass 
    if Room.objects.filter(room_name=room_name):
        pass
    else:
        Room(room_name=room_name).save()

    return render(request, 'chat/room.html', {
        'room_name_json': mark_safe(json.dumps(room_name))
    })