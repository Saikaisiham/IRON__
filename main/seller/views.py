from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import SellerRegistrationForm, SellerRegistrationUpdate
from django.contrib.auth.models import User

# ...

def register(request):
    if request.method == 'POST':
        form = SellerRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            # Create a new User instance and save it
            user = User.objects.create_user(
                username=form.cleaned_data['email'],  # Use email as the username
                email=form.cleaned_data['email'],
                password='some_password'  # You should generate a secure password
            )
            
            # Create a SellerProfile instance associated with the newly created user
            seller_profile = form.save(commit=False)
            seller_profile.user = user
            seller_profile.save()

            # Authenticate and log in the user
            user = authenticate(username=user.username, password='some_password')
            login(request, user)

            return redirect('test/')
    else:
        form = SellerRegistrationForm()

    return render(request, 'register.html', {'form': form})

# ...

def profile(request):
    if request.method == 'POST':
        form = SellerRegistrationUpdate(request.POST, request.FILES, instance=request.user.sellerprofile)
        if form.is_valid():
            form.save()
    else:
        form = SellerRegistrationUpdate(instance=request.user.sellerprofile)
    return render(request, 'profile.html', {'form': form})
