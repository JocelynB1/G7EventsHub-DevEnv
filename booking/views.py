from django.shortcuts import render
from .forms import *
from .models import *
# Create your views here.
# @login_required

def booking(request):
    location_form=LocationForm()
    event_form=EventForm()
    speaker_form=SpeakerForm()
    session_form=SessionForm()
    booking_form=BookingForm()
    
    if request.method=="POST":
        note=""
        if 'booking-form' in request.POST:
            booking_form= BookingForm(request.POST)
            if booking_form.is_valid():
                booking_form.save()
                note="Booked"
            return render(request, 
            "booking/booking.html",
            {
            'note':note,
            "event_form":event_form,
            "location_form":location_form,
            "speaker_form":speaker_form,
            "session_form":session_form,
            "booking_form":booking_form
            })
        if 'session-form' in request.POST:
            session_form= SessionForm(request.POST)
            if session_form.is_valid:
                session_form.save()
                note="New Session Type added"
            return render(request, 
            "booking/booking.html",
            {
            'note':note,
            "event_form":event_form,
            "location_form":location_form,
            "speaker_form":speaker_form,
            "session_form":session_form,
            "booking_form":booking_form
            })
        if 'event-form' in request.POST:
            event_form= EventForm(request.POST)
            if event_form.is_valid:
                event_form.save()
                note="New event added"
            return render(request, 
            "booking/booking.html",
            {
            'note':note,
            "event_form":event_form,
            "location_form":location_form,
            "speaker_form":speaker_form,
            "session_form":session_form,
            "booking_form":booking_form
            })
        if 'location-form' in request.POST:
            location_form= LocationForm(request.POST)
            if location_form.is_valid:
                location_form.save()
                note="New location added"
            return render(request, 
            "booking/booking.html",
            {
            'note':note,
            "event_form":event_form,
            "location_form":location_form,
            "speaker_form":speaker_form,
            "session_form":session_form,
            "booking_form":booking_form
            })
        if 'speaker_form' in request.POST:
            speaker_form= SpeakerForm(request.POST)
            if speaker_form.is_valid:
                speaker_form.save()
                note="New speakeer added"
            return render(request, 
            "booking/booking.html",
            {
            'note':note,
            "event_form":event_form,
            "location_form":location_form,
            "speaker_form":speaker_form,
            "session_form":session_form,
            "booking_form":booking_form
            })
        

    return render(request,"booking/booking.html",{
        "event_form":event_form,
        "location_form":location_form,
        "speaker_form":speaker_form,
        "session_form":session_form,
        "booking_form":booking_form
        })


def addBooking(request):
    booking_form=BookingForm()
    
    if request.method=="POST":
        note=""
        if 'booking-form' in request.POST:
            booking_form= BookingForm(request.POST)
            if booking_form.is_valid():
                booking_form.save()
                note="Booked"
            return render(request, 
            "booking/addBooking.html",
            {
            'note':note,
            "booking_form":booking_form
            })
    return render(request,"booking/addBooking.html",{
        "booking_form":booking_form
        })

def addLocation(request):
    location_form=LocationForm()
    
    if request.method=="POST":
        note=""
        if 'location-form' in request.POST:
            location_form= LocationForm(request.POST)
            if location_form.is_valid:
                location_form.save()
                note="New location added"
            return render(request, 
            "booking/addLocation.html",
            {
            'note':note,
            "location_form":location_form,
            })
   
    return render(request,"booking/addLocation.html",{
        "location_form":location_form,
        })

def addEvent(request):
    event_form=EventForm()
    
    if request.method=="POST":
        note=""
        if 'event-form' in request.POST:
            event_form= EventForm(request.POST)
            if event_form.is_valid:
                event_form.save()
                note="New event added"
            return render(request, 
            "booking/addEvent.html",
            {
            'note':note,
            "event_form":event_form,
            })
    
    return render(request,"booking/addEvent.html",{
        "event_form":event_form,
        })

def addSpeaker(request):
    speaker_form=SpeakerForm()
    
    if request.method=="POST":
        note=""
        if 'speaker_form' in request.POST:
            speaker_form= SpeakerForm(request.POST)
            if speaker_form.is_valid:
                speaker_form.save()
                note="New speaker added"
            return render(request, 
            "booking/addSpeaker.html",
            {
            'note':note,
            "speaker_form":speaker_form,
            })
        

    return render(request,"booking/addSpeaker.html",{
        "speaker_form":speaker_form,
        })

def addSession(request):
    session_form=SessionForm()
    
    if request.method=="POST":
        note=""
        if 'session-form' in request.POST:
            session_form= SessionForm(request.POST)
            if session_form.is_valid:
                session_form.save()
                note="New Session Type added"
            return render(request, 
            "booking/addSession.html",
            {
            'note':note,
            "session_form":session_form,
            })
   
    return render(request,"booking/addSession.html",{
        "session_form":session_form,
        })

