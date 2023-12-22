from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework import status
from django.db import IntegrityError

from backend.permissions import IsOwnerOrReadOnly
from like.models import Like
from like.serializers import LikeSerializer


class LikeList(generics.ListCreateAPIView):
    """
    List likes or create a like if logged in.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = LikeSerializer
    queryset = Like.objects.all()

    def perform_create(self, serializer):
        try:
            serializer.save(user=self.request.user)
        except IntegrityError:
            # Handle the case when the like already exists (user has already liked this post)
            existing_like = Like.objects.filter(user=self.request.user, fish_post=serializer.validated_data['fish_post']).first()
            existing_like.delete()
            return Response({'detail': 'Unliked successfully.'}, status=status.HTTP_200_OK)
