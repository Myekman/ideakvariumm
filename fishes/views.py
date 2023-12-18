from rest_framework import generics
# from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Fish
from .serializers import FishSerializer

class FishList(generics.ListCreateAPIView):
    queryset = Fish.objects.all()
    serializer_class = FishSerializer
    # permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save
    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)

   

