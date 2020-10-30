from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from datetime import datetime  

class Note(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, blank=True, null=True)
    content = RichTextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        str = ""
        if (self.title != ""):
            str = str + "Title: " + self.title + " | "
        str = str + "Content: " + self.content
        return str

class NoteLog(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, blank=True, null=True)
    content = RichTextField()
    date_log = models.DateTimeField(auto_now_add=True)

    def set_log(self, note):
        self.owner = note.owner
        self.title = note.title
        self.content = note.content

    def __str__(self):
        str = ""
        if (self.title != ""):
            str = str + "Title: " + self.title + " | "
        str = str + "Content: " + self.content
        return str