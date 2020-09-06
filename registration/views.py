from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from api.models import  Detail
from .forms import  UserRegistrationForm, UserEditForm,DetailEditForm,UserDetailFormset
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import TemplateView
from django.forms import inlineformset_factory
from django.urls import reverse
from django.contrib import messages
from django.shortcuts import redirect
from django.forms import inlineformset_factory,BaseInlineFormSet

# Create your views here.
# UserDetailFomset=inlineformset_factory(User,Detail,exclude=["id"]
# )


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
            new_user= User.objects.create()
            new_user.set_password(
                    form.cleaned_data["password"]
            )
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
    
    # def get_form_kwargs(self):
    #     kwargs = super(RegisterUserWithDetails, self).get_form_kwargs()
    #     return kwargs 

    # def add_fields(self, form, index):
    #     super(form,self).add_fields(form,index)
    #     form.fields["password"]=forms.CharField(label="Password",widget=forms.PasswordInput)
    #     form.fields["confirm_password"]=forms.CharField(label="Repeat password",widget=forms.PasswordInput)
    #     form.fields["date_of_birth"]=forms.DateField(label="Date of birth",widget=forms.SelectDateWidget)
    #     form.fields["phone_number"]=forms.CharField(label="Phone #",max_length=100)
    #     form.fields["city"]=forms.CharField(label="City",max_length=100)
    #     form.fields["address"]=forms.CharField(label="Address",max_length=500,widget=forms.Textarea)
    

    def get_success_url(self):
        return reverse("register_done")

# def invalid(request,form):
#     return render(request,"registration/register.html",{"form":form})

def register(request):
    if request.method=="POST":
        user_form=UserRegistrationForm(request.POST)
        if user_form.is_valid():
        #username
        #first_name
        #email
        #password
       #date_of_birth
       #phone_number
       #city
       #address
         items=request.POST.items()
         new_user= User.objects.create()
         new_user=user_form.save(commit=False)
         new_user.set_password(
                user_form.cleaned_data["password"]
         )
         new_user.save()
         new_detail=Detail.objects.create(user=new_user)
         new_detail.date_of_birth =user_form.cleaned_data["date_of_birth"]
         new_detail.phone_number =user_form.cleaned_data["phone_number"]
         new_detail.city =user_form.cleaned_data["city"]
         new_detail.address =user_form.cleaned_data["address"]
         new_detail.save()
         return render(request,"registration/register_done.html",{"new_user":new_user})
        #     user_form=UserRegistrationForm(request.POST)
    #     if user_form.is_valid():
    #         #Create a new user object but avoid saving it yet
    #         new_user=user_form.save(commit=False)
    #         new_user.set_password(
    #             user_form.cleaned_data["password"]
    #         )
    #         new_user.save()
    #         new_detail=Detail.objects.create(user=new_user)
    #         new_detail.date_of_birth =user_form.cleaned_data["date_of_birth"]
    #         new_detail.phone_number =user_form.cleaned_data["phone_number"]
    #         new_detail.city =user_form.cleaned_data["city"]
    #         new_detail.address =user_form.cleaned_data["address"]
    #         new_detail.save()
    #         return render(request,"registration/register_done.html",{"new_user":new_user})
    else:
         user_form=UserRegistrationForm()
    return render(request,"registration/register.html",{"user_form":user_form})

@login_required
def edit(request):
    if request.method=="POST":
        user_for=UserEditForm(instance=request.user,data=request.POST)
        detail_form=DetailEditForm(instance=request.user.Detail,
                            data=request.POST,
                            files=request.FILES)
        if user_form.is_valid() and detail_form.is_valid():
            user_form.save()
            detail_form.save()
    else:
        user_form=UserEditForm(instance=request.user)
        detail_form=DetailEditForm(instance,request.user.Detail)
    return render(request,"registration/edit.html",
                            {"user_form":user_form,
                            "detail_form":detail_form})

class UserCreateView(CreateView):
    Model=User
    exclude=["id"]

class DetailCreateView(CreateView):
    Model=Detail
    exclude=["id","created_at","updated_at"]