from django import forms

from .models import Blog, Entry

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = [
            'name',
            'description'
        ]


class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = [
            'title',
            'text',
            'img',
            'tags'
        ]