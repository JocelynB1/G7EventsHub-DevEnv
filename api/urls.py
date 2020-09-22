from django.urls import path,include

from .views import *
from rest_framework import routers
router=routers.DefaultRouter()
router.register("users",UserViewSet)
router.register("details",DetailViewSet)
urlpatterns=[
    path("register/",SignupCreateView.as_view()),
    path("location/",LocationCreateView.as_view()),
    path("event/",EventCreateView.as_view()),
    path("eventlist/",EventList.as_view()),
    path("myevents/",MyEventList.as_view()),
    path("sessionlist/",SessionList.as_view()),
    path("bookinglist/",BookingList.as_view()),
    path("locationlist/",LocationList.as_view()),
    path("eventlist/",EventList.as_view()),
    path("session/",SessionCreateView.as_view()),
    path("speaker/",SpeakerCreateView.as_view()),
    path("booking/",BookingCreateView.as_view()),
    path("<int:pk>", DetailDetails.as_view()),
    # path("details/",ListDetails.as_view()),
    path("",include(router.urls))
    
]