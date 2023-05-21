from django.http import HttpResponse

from .models import Event
from .serializers import EventSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


def index(request):
    return HttpResponse("Hello events!");

@api_view(['GET'])
def all(request):
    events = Event.objects.all()
    serializer = EventSerializer(events, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def get(request, id):
    try:
        event = Event.objects.get(id=id)
        serializer = EventSerializer(event)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Event.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def add(request):
    serializer = EventSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update(request, id):
    try:
        event = Event.objects.get(id=id)
        serializer = EventSerializer(event, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
    except Event.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete(request, id):
    try:
        event = Event.objects.get(id=id)
        event.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except Event.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    return Response(status=status.HTTP_400_BAD_REQUEST)