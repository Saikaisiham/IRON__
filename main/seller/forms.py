from django import forms
from .models import SellerProfile
from django.contrib.auth.forms import AuthenticationForm


class SellerRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta: 
        model = SellerProfile
        fields = ['first_name', 'last_name','cni', 'email', 'image', 'address', 'phone_number', 'password']




class LoginForm(forms.Form):
    email = forms.EmailField()
    cni = forms.CharField(widget=forms.PasswordInput())
    
    class Meta : 
        fields = ['email', 'cni']