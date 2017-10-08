from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from .serializers import RecordSerializer, UserSerializer, UserCreateSerializer, UserUpdateSerializer
from .permissions import IsAdmin, IsManager, IsUser
from .models import Record, User

class RecordViewSet(ModelViewSet):
  queryset = Record.objects.all()
  serializer_class = RecordSerializer

class UserViewSet(ModelViewSet):
  queryset= User.objects.all()
  serializers = {
    'POST': UserCreateSerializer,
    'PUT': UserUpdateSerializer,
    'PATCH': UserUpdateSerializer,
    'DEFAULT': UserSerializer,
  }
  permission_class = [IsAdmin, IsManager]

  def get_serializer_class(self):
    return self.serializers.get(self.request.method, self.serializers['DEFAULT'])
