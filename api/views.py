from django.shortcuts import render
from .models import Detail
from rest_framework import generics,permissions,viewsets
from rest_framework.generics import CreateAPIView
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token 
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializers import LoginSerializer ,SignUpSerializer, DetailSerializer,DeetsSerializer
from rest_framework.response import Response
from rest_framework import status
from django.db import transaction
# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset=User.objects.all()
    serializer_class=LoginSerializer

class ListDetails(generics.ListAPIView):
    queryset=Detail.objects.all()
    serializer_class=DetailSerializer

class DetailDetails(generics.RetrieveAPIView):
    queryset=Detail.objects.all()
    serializer_class=DetailSerializer


class SignUpViewSet(viewsets.ModelViewSet):
    queryset=User.objects.all()
    serializer_class=SignUpSerializer

class DetailViewSet(viewsets.ModelViewSet):
    queryset = Detail.objects.all()
    serializer_class = DetailSerializer
    # authentication_classes = [TokenAuthentication, ]
    # permission_classes = [IsAuthenticated, ]

class SignupCreateView(CreateAPIView):
    serializer_class = SignUpSerializer

    @transaction.atomic
    def post(self, request, *args, **kwrgs):

      serializer1 = SignUpSerializer(data=request.data)
      data=request.data
      user= User()
      user.username=data["username"]
      user.first_name=data["first_name"]
      user.last_name=data["last_name"]
      user.set_password(data["password"])
      user.email=data["email"]
 
 
      if serializer1.is_valid(raise_exception=True):
          detail = Detail(user=user)
          serializer2 = DeetsSerializer(user,data=request.data)
          if serializer2.is_valid(raise_exception=True):
               detail.date_of_birth=data['date_of_birth']
               detail.phone_number=data["phone_number"]
               detail.city=data["city"]
               detail.address=data["address"]
               user.save()
               detail.save()
               return Response(status=status.HTTP_200_OK)
      transaction.rollback()