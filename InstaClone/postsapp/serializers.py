from rest_framework import serializers
from .models import PostUpload

class PostUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostUpload
        fields = '__all__'
        