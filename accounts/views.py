# accounts/views.py

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status
from .serializers import LoginSerializer

class LoginView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        owner = serializer.validated_data['owner']
        token, created = Token.objects.get_or_create(owner=owner)
        return Response({'token': token.key, 'owner_id': owner.pk, 'username': owner.username}, status=status.HTTP_200_OK)
