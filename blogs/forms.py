from django import forms

from .models import Blog, Entry, Tag

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
            'tags'
        ]

        widget = {
            'tags': forms.ModelMultipleChoiceField(queryset=Tag.objects.all()),
        }