from django.urls import path
from django.contrib.auth import views as auth_views
from .import views

urlpatterns=[
    #post views
    path('booking/',views.booking,name="booking"),
    path('addEvent/',views.addEvent,name="addEvent"),
    path('addSession/',views.addSession,name="addSession"),
    path('addSpeaker/',views.addSpeaker,name="addSpeaker"),
    path('addLocation/',views.addLocation,name="addLocation"),
    path('addBooking/',views.addBooking,name="addBooking"),
    path('booking/',views.booking,name="booking"),
    
]