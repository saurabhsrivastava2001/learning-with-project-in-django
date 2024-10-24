from django.shortcuts import render

rooms=[
    {'id':1,'name':'learning phase of python django'},
    {'id':2,'name':'not in one day '},
    {'id':3,'name':'but one day for sure'},
]

# Create your views here.
def home(request):
    return render(request,'home.html',{'rooms':rooms})

def room(request):
    return render(request,'room.html')

    