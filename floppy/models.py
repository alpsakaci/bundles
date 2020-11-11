from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from datetime import datetime  
from django.utils import timezone
from django.utils.translation import gettext, gettext_lazy as _
from django.db.models import Q

CHANGE = 1
DELETION = 2

ACTION_FLAG_CHOICES = (
    (CHANGE, _('Change')),
    (DELETION, _('Deletion')),
)

class Note(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, blank=True, null=True)
    content = RichTextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(default=datetime.now, blank=True)
    deleted = models.BooleanField(default=False)

    @staticmethod
    def create(owner, title, content):
        note = Note.objects.create(owner=owner, title=title, content=content)
        caretaker = NoteCareTaker(note=note)
        caretaker.save()
        return note

    @staticmethod
    def get_user_notes(user):
        return Note.objects.filter(owner = user).order_by('date_modified').reverse()
    
    @staticmethod
    def search(user, query):
        return Note.objects.filter(Q(owner=user) & (Q(title__icontains=query) | Q(content__icontains=query)))

    def __str__(self):
        str = ""
        if (self.title != ""):
            str = str + "Title: " + self.title + " | "
        str = str + "Content: " + self.content
        return str

class NoteCareTaker(models.Model):

    note = models.OneToOneField(
        Note,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    
    def add(self, memento):
        memento.care_taker = self
        memento.save()

class NoteMemento(models.Model):
    title = models.CharField(max_length=50, blank=True, null=True)
    content = RichTextField()
    date_created = models.DateTimeField(auto_now_add=True)
    care_taker = models.ForeignKey(NoteCareTaker, on_delete=models.CASCADE)
