from django.shortcuts import render, redirect
from products.models import Product
from categories.models import Category
from django.http import JsonResponse
import requests


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


def proxy_view(request):
    if request.method == 'POST':
       
        data = request.body
        backend_url = 'http://localhost:8000/cart/add_to_cart/'

        response = requests.post(backend_url, data=data)

       
        return JsonResponse(response.json())
    else:
        return JsonResponse({'error': 'Invalid request method.'}, status=405)
