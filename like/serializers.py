from rest_framework import serializers
from .models import Like

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        user = serializers.ReadOnlyField(source='user.username')
        
        model = Like
        fields = '__all__'  
