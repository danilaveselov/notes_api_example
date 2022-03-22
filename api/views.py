from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import NoteSerializer

from .models import Note


@api_view(['GET'])
def apiMain(request):
    api_urls = {
        'List':'/note_list/',
        'Detail View':'/note_detail/<str:pk>/',
        'Create':'/note_create/',
        'Update':'/note_update/<str:pk>/',
        'Delete':'/note_delete/<str:pk>/',
        }

    return Response(api_urls)

@api_view(['GET'])
def noteList(request):
    notes = Note.objects.all().order_by('created_at')
    serializer = NoteSerializer(notes, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def noteDetail(request, pk):
    note = Note.objects.all().get(id=pk)
    serializer = NoteSerializer(note, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def noteCreate(request):
    serializer = NoteSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['POST'])
def noteUpdate(request, pk):
    note = Note.objects.get(id=pk)
    serializer = NoteSerializer(instance=note, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
def noteDelete(request, pk):
    note = Note.objects.get(id=pk)
    note.delete()

    return Response('Note has been deleted successfully!')
