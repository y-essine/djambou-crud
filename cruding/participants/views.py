from django.shortcuts import render
from django.http import HttpResponse
# import the Participant model and return all participants
from .models import Participant

def index(request):
    return HttpResponse("Hello world!")

def list(request):
    participants = Participant.objects.all()
    return HttpResponse({'participants': participants})