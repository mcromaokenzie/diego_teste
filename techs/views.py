from django.shortcuts import render
from rest_framework import generics
from .models import Tech
from .serializers import TechSerializer
from users.permissions import IsSuperUser

# Create your views here.


class TechView(generics.ListCreateAPIView):
    queryset = Tech
    serializer_class = TechSerializer

    def get_queryset(self):
        return Tech.objects.all()

    permission_classes = [IsSuperUser]


class TechDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tech
    serializer_class = TechSerializer

    permission_classes = [IsSuperUser]
