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
#Used for login
class UserViewSet(viewsets.ModelViewSet):
    queryset=User.objects.all()
    serializer_class=LoginSerializer
#Used for sign up
class SignUpViewSet(viewsets.ModelViewSet):
    queryset=User.objects.all()
    serializer_class=SignUpSerializer

class DetailDetails(generics.RetrieveAPIView):
    queryset=Detail.objects.all()
    serializer_class=DetailSerializer


#Enables the loged in user to see their profile
class DetailViewSet(viewsets.ModelViewSet):
    queryset=Detail.objects.all()
    def get_queryset(self):
        user = self.request.user
        return  Detail.objects.filter(user=user)
    serializer_class = DetailSerializer
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsAuthenticated, ]
#Used for signup
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
               user.save()
               detail.save()
               return Response(status=status.HTTP_200_OK)
      transaction.rollback()

#Used to enable the user to book an event
class BookingCreateView(CreateAPIView):
    serializer_class = BookingSerializer

    def create(self, request, *args, **kwargs): 
        data=request.data
        booking_data={}
        booking_data["user"]=request.user.id
        booking_data["event"]=data.get("id_event")
        booking_data["seats"]=data.get("seats")


        
        serializer=BookingSerializer(data=data)
    
        if serializer.is_valid(raise_exception=True):
            booking=Booking()
            booking.user=request.user
            booking.event=Event.objects.get(pk=data.get("event"))
            booking.seats=data.get("seats")
            booking.save()
        return Response()

# class BookingCreateView(CreateAPIView):
#     serializer_class = Booking1Serializer

#     def create(self, request, *args, **kwargs): 
#         data=request.data
#         booking_data={}
#         booking_data["user"]=request.user.id
#         booking_data["event"]=data.get("id_event")
#         booking_data["session"]=data.get("id_session")
#         booking_data["seats"]=data.get("seats")


#         booking1_data={}
#         booking1_data["user"]=request.user.id
#         booking1_data["event"]=data.get("id_event1")
#         booking1_data["session"]=data.get("id_session1")
#         booking1_data["seats"]=data.get("seats1")

#         booking2_data={}
#         booking2_data["user"]=request.user.id
#         booking2_data["event"]=data.get("id_event2")
#         booking2_data["session"]=data.get("id_session2")
#         booking2_data["seats"]=data.get("seats2")

#         serializer=BookingSerializer(data=data)
#         serializer1=BookingSerializer(data=booking1_data)
#         serializer2=BookingSerializer(data=booking2_data)

#         if serializer.is_valid(raise_exception=True) and serializer1.is_valid(raise_exception=True) and serializer2.is_valid(raise_exception=True):
#             booking=Booking()
#             booking1=Booking()
#             booking2=Booking()
#             booking.user=request.user
#             booking.event=Event.objects.get(pk=data.get("event"))
#             booking.session=Session.objects.get(pk=data.get("session"))
#             booking.seats=data.get("seats")
#             booking1.user=request.user
#             booking1.event=Event.objects.get(pk=data.get("id_event1"))
#             booking1.session=Session.objects.get(pk=data.get("id_session1"))
#             booking1.seats=data.get("seats1")
#             booking2.user=request.user
#             booking2.event=Event.objects.get(pk=data.get("id_event2"))
#             booking2.session=Session.objects.get(pk=data.get("id_session2"))
#             booking2.seats=data.get("seats2")
#             booking.save()
#             booking1.save()
#             booking2.save()
#         return Response()
  

#used to retrieve all events
class EventList(ListAPIView):
    serializer_class = EventSerializer
    queryset=Event.objects.all()
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsAuthenticated, ]
#used to retreive a list of events booked by the user
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

    
class MorningEventList(ListAPIView):
    serializer_class = EventSerializer
    def get_queryset(self):
        user = self.request.user
        if Booking.objects.filter(user=user.id).filter(event__session="Morning").exists():
            event_id=Booking.objects.filter(user=user.id).filter(event__session="Morning").first().event.id
            return Event.objects.filter(id=event_id)
        return Event.objects.filter(session="Morning")
        
     

    authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsAuthenticated, ]
    

class MidmorningEventList(ListAPIView):
    serializer_class = EventSerializer
    def get_queryset(self):
        user = self.request.user
        if Booking.objects.filter(user=user.id).filter(event__session="Midmorning").exists():
            event_id=Booking.objects.filter(user=user.id).filter(event__session="Midmorning").first().event.id
            return Event.objects.filter(id=event_id)
            
        return Event.objects.filter(session="Midmorning")

    authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsAuthenticated, ]


class AfternoonEventList(ListAPIView):
    serializer_class = EventSerializer
    def get_queryset(self):
        user = self.request.user
        if Booking.objects.filter(user=user.id).filter(event__session="Afternoon").exists():
            event_id=Booking.objects.filter(user=user.id).filter(event__session="Afternoon").first().event.id
            return Event.objects.filter(id=event_id)
        return Event.objects.filter(session="Afternoon")
        
        
       

    authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsAuthenticated, ]
