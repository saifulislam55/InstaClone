from . models import Story, StoryView
from django import forms


class StoryForm(forms.ModelForm):
    class Meta:
        model = Story
        fields = ['image', 'caption']
