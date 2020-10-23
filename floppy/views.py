from datetime import datetime

from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from rest_framework import routers, serializers, viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication

from .models import Note
from .serializers import NoteSerializer
from .forms import NoteForm

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

@login_required(login_url='/admin/login')
def index(request):
    notes = Note.objects.filter(owner = request.user).order_by('date_modified').reverse()
    context = {'notes': notes}

    return render(request, 'floppy/index.html', context)

@login_required(login_url='/admin/login')
def new(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)

        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            new_note = Note(owner=request.user, title=title, content=content)
            new_note.save()

            return redirect(index)
    else:
        form = NoteForm()
        context = {'form': form}

    return render(request, 'floppy/new.html', context)

@login_required(login_url='/admin/login')
def edit(request, note_id):
    if request.method == 'POST':
        form = NoteForm(request.POST)

        if form.is_valid():
            note = get_object_or_404(Note.objects.filter(id=note_id))
            # TODO: persist note to deleted notes
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            
            note.title = title
            note.content = content
            note.date_modified = datetime.now()
            note.save()

            return redirect(index)
    else:
        note = get_object_or_404(Note.objects.filter(id=note_id))
        form = NoteForm(initial={'title':note.title, 'content':note.content})
        context = {'form': form, 'note':note}

    return render(request, 'floppy/edit.html', context)

@login_required(login_url='/admin/login')
def delete(request, note_id):
    # TODO: persist note to deleted notes
    note = get_object_or_404(Note.objects.filter(id=note_id))
    note.delete()

    return redirect(index)

