from django.shortcuts import render

rooms=[
    {'id':1,'name':'learning phase of python django'}   
]

# Create your views here.
def home(request):
    return render(request,'home.html')

def room(request):
    return render(request,'room.html')

    