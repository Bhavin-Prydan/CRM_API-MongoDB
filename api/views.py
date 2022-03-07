from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserSerializer
# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer
	
	# def get_queryset(self):
	# 	# print(self.request.user)
	# 	user = User.objects.filter(username=self.request.user) 
	# 	return user