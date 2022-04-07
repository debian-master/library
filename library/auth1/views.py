from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .serializers import SignupSerializer
from auth1.models import Admin

class SignupView(generics.CreateAPIView):
    queryset = Admin.objects.all()
    serializer_class = SignupSerializer
    permission_classes = (AllowAny, )

