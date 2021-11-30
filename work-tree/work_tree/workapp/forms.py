from django import forms
from django.contrib.auth.models import User
from django.forms import fields
from . import models



class MonthlyReportForm(forms.ModelForm):
    class Meta:
        model = models.MonthlyReport 
        fields ='__all__'




class DialyNotesForm(forms.ModelForm):
    class Meta:
        model = models.DailyNotes
        fields = '__all__'



class MonthTasksForm(forms.ModelForm):
    class Meta:
        model = models.MonthMenets
        fields = '__all__'
        
        
        
        
class CustomerRegistrationForm(forms.ModelForm):
    username=forms.CharField(widget=forms.TextInput())
    password=forms.CharField(widget=forms.PasswordInput())
    email= forms.EmailField()
    class Meta():
        model= models.Customer
        fields=["username", "password", "email", "full_name", "address"]

    def clean_username(self):
        uname=self.cleaned_data.get('username')
        if User.objects.filter(username=uname).exists():
            raise forms.ValidationError("Customer with this name is already Exists!,please choose another one.")

        return uname
    def clean_email(self):
        uemail=self.cleaned_data.get("email")
        if User.objects.filter(email=uemail).exists():
            raise forms.ValidationError("This Email is already Exists!, plaease choose an other email!")
        return uemail


class CustomerloginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput())
    password=forms.CharField(widget=forms.PasswordInput())






class PasswordForgotForm(forms.Form):
    email= forms.CharField(widget=forms.EmailInput(attrs={
        "class":"form-control",
        "placeholder":"Enter the Email used in Customer account.."
    }))

    def clean_email(self):
        e = self.cleaned_data.get("email")
        if models.Customer.objects.filter(user__email=e).exists():
            pass
        else:
            raise forms.ValidationError("Customer with this Email does not exist...")
        return e 


