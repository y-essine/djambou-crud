from django.shortcuts import render
from django.http import HttpResponse
# import json to return json response
import json
# import the Event model and return all events
from .models import Event

def index(request):
    return HttpResponse("Hello events!");

def all(request):
    events = Event.objects.all()
    return HttpResponse(events.to_json(), status=200)

def add(request, body):
    event = Event.objects.create(body=body)
    return HttpResponse({'event': event.to_dict()})
