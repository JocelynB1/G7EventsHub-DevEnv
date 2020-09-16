from django.urls import path
from django.contrib.auth import views as auth_views
from .import views

urlpatterns=[
    #post views
     path('bookingDashboard/',views.booking,name="bookingDashboard"),
    path('addEvent/',views.addEvent,name="addEvent"),
    path('addSession/',views.addSession,name="addSession"),
    path('addSpeaker/',views.addSpeaker,name="addSpeaker"),
    path('addLocation/',views.addLocation,name="addLocation"),
    path('addBooking/',views.addBooking,name="addBooking"),
    path('booking/',views.booking,name="booking"),
    path('showEvents/', views.EventListView.as_view(), name='events'),
    path("booking/event/update/<int:pk>", views.EventUpdateView.as_view(),name="updateEvent"),
    path("booking/event/delete/<int:pk>", views.EventDeleteView.as_view(),name="deleteEvent"),
    path('showBooking/', views.BookingListView.as_view(), name='booking'),
    path("booking/booking/update/<int:pk>", views.BookingUpdateView.as_view(),name="updateBooking"),
    path("booking/booking/delete/<int:pk>", views.BookingDeleteView.as_view(),name="deleteBooking"),
    path('showLocation/', views.LocationListView.as_view(), name='location'),
    path("booking/location/update/<int:pk>", views.LocationUpdateView.as_view(),name="updateLocation"),
    path("booking/location/delete/<int:pk>", views.LocationDeleteView.as_view(),name="deleteLocation"),
    path('showSession/', views.SessionListView.as_view(), name='session'),
    path("booking/session/update/<int:pk>", views.SessionUpdateView.as_view(),name="updateSession"),
    path("booking/session/delete/<int:pk>", views.SessionDeleteView.as_view(),name="deleteSession"),
    path('showSpeaker/', views.SpeakerListView.as_view(), name='speaker'),
    path("booking/speaker/update/<int:pk>", views.SpeakerUpdateView.as_view(),name="updateSpeaker"),
    path("booking/speaker/delete/<int:pk>", views.SpeakerDeleteView.as_view(),name="deleteSpeaker"),
   
    # path("booking/booking/update/<int:pk>", views.BookingUpdateView.as_view(),name="updateBooking"),
    
]