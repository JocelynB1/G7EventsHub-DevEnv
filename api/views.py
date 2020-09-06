from django.shortcuts import render
from .models import Detail
from .serializers import DetailSerializer
from rest_framework import generics,permissions,viewsets
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token 
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .serializers import UserSerializer
# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset=User.objects.all()
    serializer_class=UserSerializer

class ListDetails(generics.ListAPIView):
    queryset=Detail.objects.all()
    serializer_class=DetailSerializer

class DetailDetails(generics.RetrieveAPIView):
    queryset=Detail.objects.all()
    serializer_class=DetailSerializer


class DetailViewSet(viewsets.ModelViewSet):
    queryset = Detail.objects.all()
    serializer_class = DetailSerializer
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsAuthenticated, ]