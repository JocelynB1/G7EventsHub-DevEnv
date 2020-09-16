from django.shortcuts import render
from .forms import *
from .models import *
from django.views import generic
from django.contrib.auth.decorators import login_required 
from django.utils.decorators import method_decorator
# Create your views here.

@login_required
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
            if session_form.is_valid():
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
            if event_form.is_valid():
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
            if location_form.is_valid():
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
            if speaker_form.is_valid():
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

@login_required
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
@login_required
def addLocation(request):
    location_form=LocationForm()
    
    if request.method=="POST":
        note=""
        if 'location-form' in request.POST:
            location_form= LocationForm(request.POST)
            if location_form.is_valid():
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
@login_required
def addEvent(request):
    event_form=EventForm()
    
    if request.method=="POST":
        note=""
        if 'event-form' in request.POST:
            event_form= EventForm(request.POST)
            if event_form.is_valid():
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
@login_required
def addSpeaker(request):
    speaker_form=SpeakerForm()
    
    if request.method=="POST":
        note=""
        if 'speaker_form' in request.POST:
            speaker_form= SpeakerForm(request.POST)
            if speaker_form.is_valid():
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
@login_required
def addSession(request):
    session_form=SessionForm()
    
    if request.method=="POST":
        note=""
        if 'session-form' in request.POST:
            session_form= SessionForm(request.POST)
            if session_form.is_valid():
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

@method_decorator(login_required(login_url='/login/'), name='dispatch')
class EventListView(generic.ListView ):
    Model=Event
    queryset=Event.objects.all()
    paginate_by = 25
    template_name="booking/showEvent.html"
    context_object_name = 'events' 

@method_decorator(login_required(login_url='/login/'), name='dispatch')
class EventUpdateView(generic.UpdateView):
    Model=Event
    fields=["location","name","tag_line","title","start_date","start_hour","start_minutes","end_date","end_hour","end_minutes"]
    queryset=Event.objects.all() 
    template_name="booking/updateEvent.html"
    success_url="/showEvents"

@method_decorator(login_required(login_url='/login/'), name='dispatch')
class EventDeleteView(generic.DeleteView):
    Model=Event
    queryset=Event.objects.all() 
    success_url="/showEvents"

@method_decorator(login_required(login_url='/login/'), name='dispatch')
class BookingListView(generic.ListView ):
    Model=Booking
    queryset=Booking.objects.all()
    paginate_by = 25
    template_name="booking/showBooking.html"
    context_object_name = 'booking' 

@method_decorator(login_required(login_url='/login/'), name='dispatch')
class BookingUpdateView(generic.UpdateView):
    Model=Booking
    fields=["user","event","session","seats"]
    queryset=Booking.objects.all() 
    template_name="booking/updateBooking.html"
    success_url="/showBooking"

@method_decorator(login_required(login_url='/login/'), name='dispatch')    
class BookingDeleteView(generic.DeleteView):
    Model=Booking
    queryset=Booking.objects.all() 
    success_url="/showBooking"

@method_decorator(login_required(login_url='/login/'), name='dispatch')
class LocationListView(generic.ListView ):
    Model=Location
    queryset=Location.objects.all()
    paginate_by = 25
    template_name="booking/showLocation.html"
    context_object_name = 'location' 

@method_decorator(login_required(login_url='/login/'), name='dispatch')
class LocationUpdateView(generic.UpdateView):
    Model=Location
    fields=["name","city","address","room_capacity"]
    queryset=Location.objects.all() 
    template_name="booking/updateLocation.html"
    success_url="/showLocation"

@method_decorator(login_required(login_url='/login/'), name='dispatch')
class LocationDeleteView(generic.DeleteView):
    Model=Location
    queryset=Location.objects.all() 
    success_url="/showLocation"

@method_decorator(login_required(login_url='/login/'), name='dispatch')
class SessionListView(generic.ListView ):
    Model=Session
    queryset=Session.objects.all()
    paginate_by = 25
    template_name="booking/showSession.html"
    context_object_name = 'session' 

@method_decorator(login_required(login_url='/login/'), name='dispatch')
class SessionUpdateView(generic.UpdateView):
    Model=Session
    fields=["description"]
    queryset=Session.objects.all() 
    template_name="booking/updateSession.html"
    success_url="/showSession"

@method_decorator(login_required(login_url='/login/'), name='dispatch')
class SessionDeleteView(generic.DeleteView):
    Model=Session
    queryset=Session.objects.all() 
    success_url="/showSession"

@method_decorator(login_required(login_url='/login/'), name='dispatch')
class SpeakerListView(generic.ListView ):
    Model=Speaker
    queryset=Speaker.objects.all()
    paginate_by = 25
    template_name="booking/showSpeaker.html"
    context_object_name = 'speaker' 

@method_decorator(login_required(login_url='/login/'), name='dispatch')
class SpeakerUpdateView(generic.UpdateView):
    Model=Speaker
    fields=["name","phone_number","email"]
    queryset=Speaker.objects.all() 
    template_name="booking/updateSpeaker.html"
    success_url="/showSpeaker"

@method_decorator(login_required(login_url='/login/'), name='dispatch')
class SpeakerDeleteView(generic.DeleteView):
    Model=Speaker
    queryset=Speaker.objects.all() 
    success_url="/showSpeaker"


    

    
