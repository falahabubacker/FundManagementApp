from django.shortcuts import render
from .models import Event

def home(request):
    context = {
        'events': Event.objects.all()
    }
    return render(request, 'home.html', context)

def details(request, id):
    context = {
        'event': Event.objects.get(id=id)
    }
    
    print(Event.objects.get(id=id))
    
    return render(request, 'event-details.html', context)

def add(request):
    return render(request, 'event-add.html')