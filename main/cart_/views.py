from django.shortcuts import render
from .models import Cart, CartItem
from django.http import JsonResponse
import json
from products.models import Product
from .models import Cart

def cart(requset):
    context = {}
    return render(request, 'shoping_cart.html', context)

def add_to_cart(request):
    data =json.loads(request.body)
    product_id = data['id']
    product = Product.objects.get(id=product_id)
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user, completed=False)
        print(cart)
    return JsonResponse('test', safe=False)
