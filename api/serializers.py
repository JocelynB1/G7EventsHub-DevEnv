from rest_framework import serializers 
from rest_framework.response import Response 
from rest_framework.serializers import ValidationError
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import Detail
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import password_validation
from django.http import JsonResponse
from django.core import validators


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=("id","username","password")
        extra_kwargs={"password":{"write_only":True,"required":True}}

    def create(self,validated_data):
        user=User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user


class SignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=("id","username","password","first_name","last_name","email")
        extra_kwargs={"password":{"write_only":True,"required":True}}
    

    # def create(self,validated_data):
    #     user=User.objects.create_user(**validated_data)
    #     Token.objects.create(user=user)
    #     return user

class DeetsSerializer(serializers.ModelSerializer):
    phone_number=serializers.IntegerField()
    date_of_birth=serializers.DateField(input_formats=['%Y-%m-%d'])
    class Meta:
        model = Detail
        fields=("date_of_birth","phone_number","city","address")
        

class RegistrationSerializer(serializers.ModelSerializer):
    details=serializers.SerializerMethodField()
    class Meta:
        model=User
        fields=("details","id","username","password","first_name","last_name","email")
        extra_kwargs={"password":{"write_only":True,"required":True}}

    def get_details(self,instance):
        detail=Detail.objects.get(user_id=instance.user_id)
        return DeetsSerializer(detail).data
        
        def create(self, validated_data):
                   # SignUpSerializer(validated_data)
                   pass
            # user=      UserSerializer.create(  username=validated_data["username"],
            #         first_name=validated_data["first_name"],
            #         last_name=validated_data["last_name"],
            #         password=validated_data["password"],
            #         email=validated_data["email"]
            # )
    
class DetailSerializer(serializers.ModelSerializer):
    user=serializers.SerializerMethodField()
  #  authentication_classes={TokenAuthentication,}
  #  permission_classes={IsAuthenticated,}
    #user = UserSerializer(read_only = False)

    class Meta:
        model = Detail
        fields=("user","date_of_birth","phone_number","city","address")

    def get_user(self,obj):
        user= Detail.objects.get(user_id=obj.user_id).user
        return SignUpSerializer(user).data

    def get_first_name(self,obj):
        return Detail.objects.get(user_id=obj.user_id).user.first_name

    def get_last_name(self,obj):
        return Detail.objects.get(user_id=obj.user_id).user.last_name

    def get_email(self,obj):
        return Detail.objects.get(user_id=obj.user_id).user.email

    def get_username(self,obj):
        return Detail.objects.get(user_id=obj.user_id).user.username

    def get_password(self,obj):
        return Detail.objects.get(user_id=obj.user_id).user.password

    def validate_username(self, value):
        try:
            self.full_clean()
        except ValidationError as e:
                return JsonResponse(e.message_dict, safe=False)
        except Exception as e:
                a= str(e)
        
        return Response(a)
            
        raise ValidationError()
        
    def validate_password(self,value):
        # raise ValidationError("???ihoihj?")

        try:
            password_validation.validate_password(value, self.instance)
        except ValidationError:
             raise serializers.ValidationError.messages[0]
        return (value)

    def create(self, validated_data):
    #     a=[]
    #     a.append(validated_data["username"])
    #     if UserSerializer(data=a).is_valid():
            user_data = validated_data['user']
            user=      UserSerializer.create(  username=validated_data["username"],
                    first_name=validated_data["first_name"],
                    last_name=validated_data["last_name"],
                    password=validated_data["password"],
                    email=validated_data["email"]
            )
            # user= User()
            # user.username=validated_data["username"]
            # user.first_name=validated_data["first_name"]
            # user.last_name=validated_data["last_name"]
            # user.set_password(validated_data["password"])
            # user.email=validated_data["email"]
            # # try:
            #     user.full_clean()
            # except ValidationError as e:
            #        return JsonResponse(e.message_dict, safe=False)
            # except Exception as e:
            #     a= str(e)
        
            #     return Response(a)
             
            # if user.full_clean():
            # user.save()
            detail = Detail.objects.create(user=user,
                                    date_of_birth=validated_data['date_of_birth'],
                                    phone_number=validated_data["phone_number"],
                                    city=validated_data["city"],
                                    address=validated_data["address"])
            detail.save()
            return detail

    def to_internal_value(self, data):
        internal_value = super(DetailSerializer, self).to_internal_value(data)
        password = data.get("password")
        username = data.get("username")
        first_name=data.get("first_name")
        last_name=data.get("last_name")
        email=data.get("email")
        internal_value.update({
        "username": username,
        "password": password,
        "first_name":first_name,
        "last_name":last_name,
        "email":email
    })
        return internal_value
