from django import forms
from django.core import validators
from .models import *
from django.contrib.auth.models import User

class LocationForm(forms.ModelForm):
    class Meta:
        model=Location
        fields=["name","city","address","room_capacity"]
    # name=forms.CharField(label="Name of location",max_length=100)
    # city=forms.CharField(label="City",max_length=100)
    # address=forms.Textarea()
    # room_capacity=forms.IntegerField(label="Room capacity")


class EventForm(forms.ModelForm):
    start_date=forms.DateField(widget=forms.SelectDateWidget)
    end_date=forms.DateField(widget=forms.SelectDateWidget)

    class Meta:
        model=Event
        fields=["location","speaker","name","tag_line","title","start_date","start_hour","start_minutes","end_date","end_hour","end_minutes"]
        # fields=["location","name","tag_line","title","start_time","end_time"]

    # name=forms.CharField(label="Name of event",max_length=100)
    # tag_line=forms.CharField(label="Tag line",max_length=100)
    # title=forms.CharField(label="title",max_length=100)


class SpeakerForm(forms.ModelForm):
    class Meta:
        model=Speaker
        fields=["name","phone_number","email"]
    
    def clean_phone_number(self):
        cd=self.cleaned_data
        str_phonenumber=str(cd["phone_number"])
        valid_prefixes=[
            "032",
            "035",
            "033",
            "034",
            "030",
            "037",
            "038",
            "039",
            "036",
            "031",
            "023",
            "024",
            "054",
            "055",
            "059",
            "027",
            "057",
            "026",
            "056",
            "028",
            "020",
            "050"
            ]        
        if not str_phonenumber[:3] in str(valid_prefixes): 
            raise forms.ValidationError("Invalid Number"+str_phonenumber[:3])

        if len(str_phonenumber)<10:
            raise forms.ValidationError("Phone number is too short")

        if len(str_phonenumber)>10:
            raise forms.ValidationError("Phone number is too long")

        return cd["phone_number"]
    
    
    def clean_email(self):
        cd=self.cleaned_data
        value=cd["email"]    
        if Speaker.objects.filter(email=value).exists():
            raise forms.ValidationError("Email already exists.Please choose another")

    # name=forms.CharField(label="Name of speaker",max_length=100)
    # phone_number=forms.IntegerField(label="Phone #")
    # email=forms.EmailField(label="Email address of speaker")

class SessionForm(forms.ModelForm):
    class Meta:
        model=Session
        fields=["description"]
    description=forms.CharField(label="Description of session")


class BookingForm(forms.ModelForm):
    class Meta:
        model=Booking
        fields=["user","event","session","seats"]
    # user=forms.ModelChoiceField(label="Name of User",queryset=User.objects.all())
    # event=forms.ModelChoiceField(label="Name of Event",queryset=Event.objects.all())
    # session=forms.ModelChoiceField(label="Session",queryset=Session.objects.all())
    seats=forms.IntegerField(label="Seats",validators=[validators.MinValueValidator(1) ])
