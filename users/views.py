from django.shortcuts import render
from rest_framework import generics
from .models import User
from .serializers import UserSerializer
from .permissions import IsSuperUser

# Create your views here.


class UserView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    # permission_classes = [IsSuperUser]


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    permission_classes = [IsSuperUser]
