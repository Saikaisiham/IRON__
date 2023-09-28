from django.shortcuts import render, redirect
from products.models import Product
from categories.models import Category
from django.http import JsonResponse

# Create your views here.

def index(request): 
    products = Product.objects.all()
    categories = Category.objects.all()
    context = {
        'products': products,
        'categories' : categories,
    }
    # print(len(products))  
    return render(request, 'index.html', context)

def joinus(request):
    return render(request, 'joinus.html')


