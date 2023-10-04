from django.shortcuts import render, redirect
from .forms import ClientForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm

def register_page(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            print(request.POST)
            return redirect('/products')
        messages.error(request, "Unsuccessful registration. Invalid information.")
    else:
        form = ClientForm()
    return render(request, 'register_login.html', {'form': form})

def login_page(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                print(request.POST)
                messages.info(request, f'You are now logged in as {username}')
                return redirect('/')  
            else:
                messages.error(request, 'Invalid username or password')
        else:
            messages.error(request, 'Invalid username or password')
    else:
        form = AuthenticationForm()
    return render(request, 'login_register.html', {'form': form})
