from urllib import request

from django.contrib.auth import authenticate, login
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from pyexpat.errors import messages

from scrumboard.models import Room, Message, Utilizatori


# Create your views here.
def home(request):
    return render(request, 'home.html')

def room(request, room):
    username = request.GET.get('username')
    room_details = Room.objects.get(name=room)
    return render(request, 'room.html', {
        'username': username,
        'room': room,
        'room_details': room_details
    })

def checkview(request):
    room = request.POST['room_name']
    username = request.POST['username']

    if Room.objects.filter(name=room).exists():
        return redirect('/'+room+'/?username='+username)
    else:
        new_room=Room.objects.create(name=room)
        new_room.save()
        return redirect('/' + room + '/?username=' + username)

def send(request):
    message = request.POST['message']
    username = request.POST['username']
    room_id = request.POST['room_id']

    new_message = Message.objects.create(value=message, user=username, room=room_id)
    new_message.save()
    return HttpResponse('Message sent')

def getMessages(request, room):
    room_details = Room.objects.get(name=room)

    messages = Message.objects.filter(room=room_details.id)
    return JsonResponse({"messages":list(messages.values())})


def signin(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, name=username, password=password)
    if user!=None:
        login(request, user)  # request.user == user
        return redirect("/home")
            # attempt = request.session.get("attempt") or 0
            # request.session['attempt'] += 1
            # return redirect("/invalid-password")
    else:
        request.session['invalid_user'] = 1
    return render(request, 'login.html')
