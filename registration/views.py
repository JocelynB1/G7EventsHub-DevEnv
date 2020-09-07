from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from api.models import  Detail
from .forms import  UserRegistrationForm, UserDetailFormset
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import TemplateView
from django.urls import reverse
from django.shortcuts import redirect

# Create your views here.

class RegisterUserWithDetails(CreateView):
    model = User
    template_name = "registration/register.html"
    form_class = UserRegistrationForm
         
    def get_context_data(self,**kwargs):
        data=super().get_context_data(**kwargs)
        if self.request.POST:
            data["details"]=UserDetailFormset(self.request.POST)
        else:
           data["details"]=UserDetailFormset()
        return data

    def form_valid(self,form):
        context=self.get_context_data()
        details=context["details"]
        if details.is_valid():
            new_user= form.save(commit=False)
            new_user.set_password(form.cleaned_data["password"])
            new_user.save()
            new_detail=Detail.objects.create(user=new_user)
            new_detail.date_of_birth =form.cleaned_data["date_of_birth"]
            new_detail.phone_number =form.cleaned_data["phone_number"]
            new_detail.city =form.cleaned_data["city"]
            new_detail.address =form.cleaned_data["address"]
            new_detail.save()
            return super().form_valid(form)
        else:
            return render(self.request, 'registration/register.html', {'form': form,'details':details})
    def get_success_url(self):
        return reverse("register_done")




class UserCreateView(CreateView):
    Model=User
    exclude=["id"]

class DetailCreateView(CreateView):
    Model=Detail
    exclude=["id","created_at","updated_at"]