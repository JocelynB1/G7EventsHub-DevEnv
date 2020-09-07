from django.urls import path
from django.contrib.auth import views as auth_views
from .import views
from django.views.generic import TemplateView

urlpatterns=[
path("register/",views.RegisterUserWithDetails.as_view(),name="register"),
path("register_done/",TemplateView.as_view(template_name="registration/register_done.html"),name="register_done"),   
];