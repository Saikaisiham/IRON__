from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import SellerRegistrationForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .models import SellerProfile

# ...

def register(request):
    if request.method == 'POST':
        form = SellerRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data['cni'],  
                email=form.cleaned_data['email'],
                password='some_password' 
            )
            
            
            seller_profile = form.save(commit=False)
            seller_profile.user = user
            seller_profile.save()

            
            user = authenticate(username=user.username, password='some_password')
            login(request, user)

            return redirect('/products')
    else:
        form = SellerRegistrationForm()

    return render(request, 'register.html', {'form': form})




def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)  
        if form.is_valid():
            email = form.cleaned_data.get('username') 
            cni = form.cleaned_data.get('password')

            
         
            user = authenticate(request, username=email, password=cni)
            
            if user is not None:
                login(request, user)
                messages.info(request, f'You are now logged in as {email}.')
                return redirect('/products')
            else:
                messages.error(request, "Invalid username or CNI.")
                print(email)
                print(request.POST)
        else:
            messages.error(request, "Invalid username or CNI.")
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})