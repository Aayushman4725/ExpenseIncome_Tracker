from django.shortcuts import render
from .serializers import *
from rest_framework import generics
from django.contrib.auth import get_user_model
# Create your views here.
User = get_user_model()


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class= RegisterSerializer
    



