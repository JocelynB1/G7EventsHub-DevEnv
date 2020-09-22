from rest_framework import serializers 
from rest_framework.response import Response 
from rest_framework.serializers import ValidationError
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import Detail
from booking.models import *
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import password_validation
from django.http import JsonResponse
from django.core import validators


class LoginSerializer(serializers.ModelSerializer):
    """
    Used for Login only 
    """
    class Meta:
        model=User
        fields=("id","username","password")
        extra_kwargs={"password":{"write_only":True,"required":True}}

    def create(self,validated_data):
        user=User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user


class SignUpSerializer(serializers.ModelSerializer):
    """
    Used to register new users
    """
    # email=serializers.EmailField(validators =[unique-True] )
    # confirm_password=serializers.SerializerMethodField()
    class Meta:
        model=User
        fields=("id","username","password","first_name","last_name","email")
        extra_kwargs={"password":{"write_only":True,"required":True}}

    
    
    
    def validate_password(self,value):
        try:
            password_validation.validate_password(value, self.instance)
        except ValidationError:
             raise serializers.ValidationError.messages[0]
        return (value)

    def save(self, **kwargs):
        pass

class DeetsSerializer(serializers.ModelSerializer):
    """
    Used to validate additional user details recorded at signup
    """
    phone_number=serializers.IntegerField()
    date_of_birth=serializers.DateField(input_formats=['%Y-%m-%d'])
    class Meta:
        model = Detail
        fields=("date_of_birth","phone_number","city","address")
        

    
class DetailSerializer(serializers.ModelSerializer):
    """
    Used to Display user details to authenticated users
    """
    first_name=serializers.SerializerMethodField()
    last_name=serializers.SerializerMethodField()
    email=serializers.SerializerMethodField()
    username=serializers.SerializerMethodField()

    authentication_classes={TokenAuthentication,}
    permission_classes={IsAuthenticated,}

    class Meta:
        model = Detail
        fields=("user_id", "first_name","last_name","email","username","date_of_birth","phone_number","city","address")

    def get_first_name(self,obj):
        return Detail.objects.get(user_id=obj.user_id).user.first_name

    def get_user_id(self,obj):
        return obj.user_id

    def get_last_name(self,obj):
        return Detail.objects.get(user_id=obj.user_id).user.last_name

    def get_email(self,obj):
        return Detail.objects.get(user_id=obj.user_id).user.email

    def get_username(self,obj):
        return Detail.objects.get(user_id=obj.user_id).user.username

    

    def to_internal_value(self, data):
        internal_value = super(DetailSerializer, self).to_internal_value(data)
        username = data.get("username")
        first_name=data.get("first_name")
        last_name=data.get("last_name")
        email=data.get("email")
        internal_value.update({
        "username": username,
        "first_name":first_name,
        "last_name":last_name,
        "email":email
    })
        return internal_value


class LocationSerializer(serializers.ModelSerializer):
    """
    """
    class Meta:
        model = Location
        fields=["id","name","city","address","room_capacity"]

class EventSerializer(serializers.ModelSerializer):
    """
    """
    class Meta:
        model = Event
        fields=["id","location","name","tag_line","title","start_date","start_hour","start_minutes","end_date","end_hour","end_minutes"]


class SpeakerSerializer(serializers.ModelSerializer):
    """
    """
    class Meta:
        model = Speaker
        fields=["name","phone_number","email"]


class SessionSerializer(serializers.ModelSerializer):
    """
    """
    class Meta:
        model = Session
        fields=["id","description"]
        
class BookingSerializer(serializers.ModelSerializer):
    """
    """
    class Meta:
        model = Booking
        fields=["user","user_id","event","session","seats"]
    user=serializers.SerializerMethodField()

    def get_user(self,obj):
        return User.objects.get(id=obj.user_id).first_name+" "+User.objects.get(id=obj.user_id).last_name

        
class Booking1Serializer(serializers.ModelSerializer):
    """
    """
    id_session1=serializers.IntegerField()
    id_session2=serializers.IntegerField()
    id_event1=serializers.IntegerField()
    id_event2=serializers.IntegerField()
    seats1=serializers.IntegerField()
    seats2=serializers.IntegerField()
    class Meta:
        model = Booking
        fields=["event","id_event1","id_event2","session","id_session1","id_session2","seats","seats1","seats2"]
        

class Booking11Serializer(serializers.ModelSerializer):
    """
    """
    class Meta:
         model = Booking
         fields=["user","event","session","seats"]

class MyEventSerializer(serializers.ModelSerializer):
    """
    """
    location=serializers.SerializerMethodField()    
    event_name=serializers.SerializerMethodField()    
    tag_line=serializers.SerializerMethodField()    
    title=serializers.SerializerMethodField()    
    start_date=serializers.SerializerMethodField()    
    end_date=serializers.SerializerMethodField()    
    session=serializers.SerializerMethodField()    
    class Meta:
        model = Booking
        fields=["id","location","event_name","tag_line","title","start_date","end_date","session","seats"]
    def get_location(self,obj):
        return Location.objects.get(pk=obj.event.location_id).name

    def get_event_name(self,obj):
        return obj.event.name

    def get_tag_line(self,obj):
        return obj.event.tag_line

    def get_title(self,obj):
        return obj.event.title

    def get_start_date(self,obj):
       return str(obj.event.start_date)+" , "+str(obj.event.start_hour)+" : "+str(obj.event.start_minutes)

    def get_end_date(self,obj):
       return str(obj.event.end_date)+" , "+str(obj.event.end_hour)+" : "+str(obj.event.end_minutes)
    
    def get_session(self,obj):
        return obj.session.description
    
    
   







