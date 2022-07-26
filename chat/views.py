from django.shortcuts import render

from chat.models import Room, User


def index_view(request):
    return render(request, 'index.html', {
        'rooms': Room.objects.all(),
        'users': User.objects.all(),
    })


def room_view(request, room_name, user_name):
    chat_room, created = Room.objects.get_or_create(name=room_name)
    user = User.objects.create(username=user_name)
    return render(request, 'room.html', {
        'room': chat_room,
        'user': user
    })
