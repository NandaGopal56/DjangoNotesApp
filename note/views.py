import re
from urllib import response
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import NoteSerializer
from .models import Note
# Create your views here.

def func_get_notes(request):
    notes = Note.objects.all()
    serializer = NoteSerializer(notes, many=True)
    return serializer.data

def func_get_note(request, pk):
    notes = Note.objects.get(id=pk)
    serializer = NoteSerializer(notes, many=False)
    return serializer.data

def func_create_note(request):
    data = request.data
    note = Note.objects.create(body=data['body'])
    serializer = NoteSerializer(note, many=False)
    return serializer.data

def func_update_note(request, pk):
    data = request.data
    note = Note.objects.get(id=pk)
    serializer = NoteSerializer(instance=note, data=data)
    if serializer.is_valid():
        serializer.save()
    return serializer.data

def func_delete_note(request, pk):
    note = Note.objects.get(id=pk)
    note.delete()
    return 'Note was deleted'

@api_view(['GET'])
def getNotes(request):
    resp = func_get_notes(request)
    return Response(resp)

@api_view(['GET'])
def getNote(request, pk):
    resp = func_get_note(request, pk)
    return Response(resp)

@api_view(['POST'])
def createNote(request):
    resp = func_create_note(request)
    return Response(resp)

@api_view(['PUT'])
def updateNote(request, pk):
    resp = func_update_note(request, pk)
    return Response(resp)

@api_view(['DELETE'])
def deletenote(request, pk):
    resp = func_delete_note(request, pk)
    return Response(resp)

@api_view(['GET', 'PUT', 'DELETE'])
def notesapp(request, pk):
    if request.method == 'GET':
        resp = func_get_note(request, pk)
    elif request.method == 'PUT':
        resp = func_update_note(request, pk)
    elif request.method == 'DELETE':
        resp = func_delete_note(request, pk)
    return Response(resp)