from django import forms
from django.contrib.auth.models import User
from api.models import  Detail
from django.forms import inlineformset_factory,BaseInlineFormSet

UserDetailFormset=inlineformset_factory(User,Detail,exclude=(None,))

class UserDetailForm(UserDetailFormset):
    def add_fields(self, form, index):
        super(UserDetailForm,self).add_fields(form,index)
        form.fields["password"]=forms.CharField(label="Password",widget=forms.PasswordInput)
        form.fields["confirm_password"]=forms.CharField(label="Repeat password",widget=forms.PasswordInput)
        form.fields["date_of_birth"]=forms.DateField(label="Date of birth",widget=forms.SelectDateWidget)
        form.fields["phone_number"]=forms.CharField(label="Phone #",max_length=100)
        form.fields["city"]=forms.CharField(label="City",max_length=100)
        form.fields["address"]=forms.CharField(label="Address",max_length=500,widget=forms.Textarea)

    def clean_confirm_password(self):
        cd=self.cleaned_data
        if cd["password"]!=cd["confirm_password"]:
            raise forms.ValidationError("Passwords don\'t match.")
        return cd["confirm_password"]

class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model=User
        fields=("username","first_name","last_name","email")
    password=forms.CharField(label="Password",widget=forms.PasswordInput)
    confirm_password=forms.CharField(label="Repeat password",widget=forms.PasswordInput)
    date_of_birth=forms.DateField(label="Date of birth",widget=forms.SelectDateWidget)
    phone_number=forms.CharField(label="Phone #",max_length=100)
    city=forms.CharField(label="City",max_length=100)
    address=forms.CharField(label="Address",max_length=500,widget=forms.Textarea)

    def clean_confirm_password(self):
        cd=self.cleaned_data
        if cd["password"]!=cd["confirm_password"]:
            raise forms.ValidationError("Passwords don\'t match.")
        return cd["confirm_password"]
    

class UserEditForm(forms.ModelForm):
    class Meta:
        model=User
        fields=("first_name","last_name","email")

class DetailEditForm(forms.ModelForm):
    class Meta:
        model=Detail
        fields=("date_of_birth","phone_number","city","address")