from django import forms
from .models import SellerProfile


class SellerRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta: 
        model = SellerProfile
        fields = ['first_name', 'last_name','cni', 'email', 'image', 'address', 'phone_number', 'password']


class SellerRegistrationUpdate(forms.ModelForm):
    class Meta : 
        model = SellerProfile
        fields = ['first_name', 'last_name','cni', 'email', 'image', 'address' ,'phone_number']
