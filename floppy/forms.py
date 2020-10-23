from django import forms

class NoteForm(forms.Form):
    title = forms.CharField(label='Title', max_length=20)
    content = forms.CharField(label='content', max_length=100)
