from django.shortcuts import render
from django.utils.safestring import mark_safe

import json

def index(request):
    return render(request, 'chat/index.html', {})

# a room view that lets you see messages posted in a chat room.
# room view opens a WebSocket to ws://127.0.0.1:8000/ws/chat/ROOM_NAME/
def room(request, room_name):
    return render(request, 'chat/room.html', {
        'room_name_json': mark_safe(json.dumps(room_name))
    })
