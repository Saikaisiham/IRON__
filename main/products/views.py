from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm
from seller.models import SellerProfile

# Create your views here.
def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            try:
                seller_profile = SellerProfile.objects.get(user=request.user)
                product.owner = seller_profile
                product.save()
                return redirect('create_product')
            except SellerProfile.DoesNotExist:
                pass
    else:
        form = ProductForm()
    return render(request, 'create_product.html', {'form': form})
