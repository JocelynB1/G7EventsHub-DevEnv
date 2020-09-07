from django import forms
from django.contrib.auth.models import User
from api.models import  Detail
from django.forms import inlineformset_factory,BaseInlineFormSet
from django.contrib.auth.password_validation import validate_password
from django.core import validators
UserDetailFormset=inlineformset_factory(User,Detail,exclude=(None,))


class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model=User
        fields=("username","first_name","last_name","email")
    password=forms.CharField(label="Password",widget=forms.PasswordInput,validators=[validate_password])
    confirm_password=forms.CharField(label="Repeat password",widget=forms.PasswordInput,validators=[validate_password])
    date_of_birth=forms.DateField(label="Date of birth",widget=forms.SelectDateWidget)
    phone_number=forms.CharField(label="Phone #",max_length=100)
    city=forms.CharField(label="City",max_length=100)
    address=forms.CharField(label="Address",max_length=500,widget=forms.Textarea)

    def clean_confirm_password(self):
        cd=self.cleaned_data
        if cd["password"]!=cd["confirm_password"]:
            raise forms.ValidationError("Passwords don\'t match.")
        return cd["confirm_password"]
    