from rest_framework import serializers
from rest_framework.authtoken.models import Token 
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import Detail
from django.contrib.auth.models import User

class DetailSerializer(serializers.ModelSerializer):
    first_name=serializers.SerializerMethodField()
    last_name=serializers.SerializerMethodField()
    email=serializers.SerializerMethodField()
    authentication_classes={TokenAuthentication,}
    permission_classes={IsAuthenticated,}
 
    class Meta:
        model = Detail
        fields=("user","date_of_birth","phone_number","city","address","first_name","last_name","email")
        
    def get_first_name(self,obj):
        return Detail.objects.get(user_id=obj.user_id).user.first_name
    
    def get_last_name(self,obj):
        return Detail.objects.get(user_id=obj.user_id).user.last_name

    def get_email(self,obj):
        return Detail.objects.get(user_id=obj.user_id).user.email
  
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=("id","username","password")
        extra_kwargs={"password":{"write_only":True,"required":True}}

    def create(self,validated_data):
        user=User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user