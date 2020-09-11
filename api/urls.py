from django.urls import path,include

from .views import ListDetails,DetailDetails,UserViewSet,DetailViewSet,SignUpViewSet,SignupCreateView
from rest_framework import routers
router=routers.DefaultRouter()
router.register("users",UserViewSet)
router.register("details",DetailViewSet)
router.register("SignUp",SignUpViewSet)
urlpatterns=[
    path("register",SignupCreateView.as_view()),
    path("<int:pk>", DetailDetails.as_view()),
    # path("details/",ListDetails.as_view()),
    path("",include(router.urls))
    #pg54
]