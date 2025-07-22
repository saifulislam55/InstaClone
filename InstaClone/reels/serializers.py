from rest_framework import serializers
from .models import Reels


class ReelsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Reels
        fields = '__all__'        
