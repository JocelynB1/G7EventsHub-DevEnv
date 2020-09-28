from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Detail)
class DetailAdmin(admin.ModelAdmin):
    list_display=["user","date_of_birth","phone_number","city"]


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display=["name","city","address","city","room_capacity"]

@admin.register(Event)        
class EventAdmin(admin.ModelAdmin):
    list_display=["name","tag_line","title","start_date","start_hour","start_minutes","end_date","end_hour","end_minutes"]


@admin.register(Speaker)
class SpeakerAdmin(admin.ModelAdmin):
    list_display=["phone_number","name","email"]

@admin.register(Session)    
class SessionAdmin(admin.ModelAdmin):
    list_display=["description"]

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display=["user","event","session","seats"]

    


