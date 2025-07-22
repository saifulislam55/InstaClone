from django import forms
from . models import PostUpload

class PostUploadForm(forms.ModelForm):
    class Meta:
        model = PostUpload
        fields = ['caption', 'post_file',]