from django.shortcuts import render, redirect
from products.models import Product

# Create your views here.

def index(request): 
    products = Product.objects.all()
    # print(len(products))  
    return render(request, 'index.html', {'products': products})


def joinus(request):
    return render(request, 'joinus.html')


