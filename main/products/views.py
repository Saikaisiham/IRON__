from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm
from seller.models import SellerProfile

@login_required
def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            seller_profile = SellerProfile.objects.get(user=request.user)
            product.owner = seller_profile
            product.save()
            return redirect('create_product')
    else:
        form = ProductForm()
    return render(request, 'create_product.html', {'form': form})
