from django.shortcuts import render
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def confirm(request):
    return render(request,"accounts/profile/index.html")

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))
    