from django.urls import path,include

from .views import *
from rest_framework import routers
router=routers.DefaultRouter()
router.register("users",UserViewSet)
router.register("details",DetailViewSet)
urlpatterns=[
    path("register/",SignupCreateView.as_view()),
    path("eventlist/",EventList.as_view()),
    path("myevents/",MyEventList.as_view()),
    path("locationlist/",LocationList.as_view()),
    path("eventlist/",EventList.as_view()),
    path("morningeventlist/",MorningEventList.as_view()),
    path("midmorningeventlist/",MidmorningEventList.as_view()),
    path("afternooneventlist/",AfternoonEventList.as_view()),
    path("booking/",BookingCreateView.as_view()),
    path("<int:pk>", DetailDetails.as_view()),
    path("",include(router.urls)),
    # path('bookingDashboard/',views.booking,name="bookingDashboard"),

    
]