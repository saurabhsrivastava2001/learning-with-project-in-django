from django.shortcuts import render
from .models import Room
rooms=[
    {'id':1,'name':'learning phase of python django'},
    {'id':2,'name':'not in one day '},
    {'id':3,'name':'but one day for sure'},
]

# Create your views here.
def home(request):
    rooms = Room.objects.all()
    context={'rooms':rooms}
    return render(request,'base/home.html',context)

def room(request,pk):
    room=None
    for i in rooms:
        if i['id'] == int (pk):
            room=i
    context={'room':room}
    
    return render(request,'base/room.html',context)
