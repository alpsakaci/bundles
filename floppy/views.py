from django.shortcuts import get_object_or_404

from rest_framework import routers, serializers, viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication

from .models import Note
from .serializers import NoteSerializer

class NoteViewSet(viewsets.ModelViewSet):
    authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication)

    queryset = Note.objects.all()
    serializer_class = NoteSerializer

    def list(self, request):
        queryset = Note.objects.filter(owner = request.user)
        serializer = NoteSerializer(queryset, many = True)

        return Response(serializer.data)

    def retrieve(self, request, pk = None):
        queryset = Note.objects.filter(owner = request.user)
        note = get_object_or_404(queryset, pk = pk)
        serializer = NoteSerializer(note)

        return Response(serializer.data)