from django.shortcuts import render
from .models import Detail
from rest_framework import generics,permissions,viewsets
from rest_framework.generics import CreateAPIView,ListAPIView
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token 
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializers import *
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
    queryset=Detail.objects.all()
    def get_queryset(self):
        user = self.request.user
        return  Detail.objects.filter(user=user)
    serializer_class = DetailSerializer
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsAuthenticated, ]

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

class LocationCreateView(CreateAPIView):
    serializer_class = LocationSerializer

class EventCreateView(CreateAPIView):
    serializer_class = EventSerializer

class SpeakerCreateView(CreateAPIView):
    serializer_class = SpeakerSerializer

class SessionCreateView(CreateAPIView):
    serializer_class = SessionSerializer

class BookingCreateView(CreateAPIView):
    serializer_class = Booking1Serializer

    def create(self, request, *args, **kwargs): 
        data=request.data
        serializer=Booking11Serializer(data=data)
        if(True):
            booking=Booking()
            booking1=Booking()
            booking2=Booking()
            booking.user=request.user
            booking.event=Event.objects.get(pk=data.get("event"))
            booking.session=Session.objects.get(pk=data.get("session"))
            booking.seats=data.get("seats")
            booking1.user=request.user
            booking1.event=Event.objects.get(pk=data.get("id_event1"))
            booking1.session=Session.objects.get(pk=data.get("id_session1"))
            booking1.seats=data.get("seats1")
            booking2.user=request.user
            booking2.event=Event.objects.get(pk=data.get("id_event2"))
            booking2.session=Session.objects.get(pk=data.get("id_session2"))
            booking2.seats=data.get("seats2")
            booking.save()
            booking1.save()
            booking2.save()

        return Response()
  
    
class BookingList(ListAPIView):
    serializer_class = BookingSerializer
    queryset=Booking.objects.all()
    
class SessionList(ListAPIView):
    serializer_class = SessionSerializer
    queryset=Session.objects.all()
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsAuthenticated, ]

class EventList(ListAPIView):
    serializer_class = EventSerializer
    queryset=Event.objects.all()
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsAuthenticated, ]

class MyEventList(ListAPIView):
    serializer_class = MyEventSerializer
    def get_queryset(self):
        user = self.request.user
        return Booking.objects.filter(user=user.id)
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsAuthenticated, ]

  



class LocationList(ListAPIView):
    serializer_class = LocationSerializer
    queryset=Location.objects.all()
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsAuthenticated, ]

    
    
