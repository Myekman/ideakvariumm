# serializers.py
from rest_framework import serializers
from .models import Fish

class FishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fish
        fields = ['id', 'fish_type', 'message', 'like_count', 'created_at']
