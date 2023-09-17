from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm

@login_required
def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.owner = request.user.sellerprofile  
            product.save()
            return redirect('create_product')
    else:
        form = ProductForm()
    return render(request, 'create_product.html', {'form': form})
