from django.shortcuts import render
from .models import Room,Message

def HomeView(request):
    if request.method=='POST':
        username=request.POST['username']
        room=request.POST['room']
        try:
            existing_room=Room.objects.get(room_name=room)
        except Room.DoesNotExist:
            new_room=Room.objects.create(room_name=room)
    return render(request,'home.html')


def RoomView(request,room_name,username):
    return render(request,'room.html')
