from django.shortcuts import render, redirect
from products.models import Product
from categories.models import Category
from django.http import JsonResponse
from .filters import CategoryFilter
from categories.models import Category
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


def search(request):
    category_filter = CategoryFilter(request.GET, queryset=Product.objects.all())
    category_id = request.GET.get('category')

    print(f"Selected category_id: {category_id}")  # Debugging line

    if category_id:
        # Filter products by category if category_id is provided
        category = Category.objects.get(pk=category_id)
        category_filter = category_filter.qs.filter(category=category)

    # Debugging line to inspect the filtered products
    print(f"Filtered products: {list(category_filter)}")

    return render(request, 'product.html', {'filter': category_filter})
