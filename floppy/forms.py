from django import forms
from ckeditor.widgets import CKEditorWidget

from .models import Note

class NoteForm(forms.ModelForm):
    title = forms.CharField(label='Title', max_length=20)
    content = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Note
        fields = ['title', 'content']
