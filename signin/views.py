from django.shortcuts import render

# Create your views here.
def confirm(request):
    return render(request,"accounts/profile/index.html")