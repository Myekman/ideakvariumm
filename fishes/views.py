from rest_framework import generics, permissions
from .models import Fish
from .serializers import FishSerializer

class FishList(generics.ListCreateAPIView):
    queryset = Fish.objects.all()
    serializer_class = FishSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly] # Allow GET for everyone, require authentication for POST

        
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

   

