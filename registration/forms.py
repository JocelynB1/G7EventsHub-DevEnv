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
    
        def clean_phone_number(self):
            cd=self.cleaned_data
        str_phonenumber=str(cd["phone_number"])
        valid_prefixes=[
            "032",
            "035",
            "033",
            "034",
            "030",
            "037",
            "038",
            "039",
            "036",
            "031",
            "023",
            "024",
            "054",
            "055",
            "059",
            "027",
            "057",
            "026",
            "056",
            "028",
            "020",
            "050"
            ]        
        if not str_phonenumber[:3] in str(valid_prefixes): 
            raise forms.ValidationError("Invalid Number")

        if len(str_phonenumber)<10:
            raise forms.ValidationError("Phone number is too short")

        if len(str_phonenumber)>10:
            raise forms.ValidationError("Phone number is too long")

        return cd["phone_number"]

    
    