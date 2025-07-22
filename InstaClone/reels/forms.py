from django import forms
from .models import Reels, Comment


class ReelUploadForm(forms.ModelForm):
    class Meta:
        model = Reels
        fields = ['caption','reel_file']


from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={
                'class': 'w-full border rounded p-2',
                'placeholder': 'Add a comment...',
                'rows': 2
            })
        }
