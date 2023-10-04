from django.shortcuts import render, redirect
from .models import Cart, CartItem
from products.models import Product

def cart_view(request):
    cart = Cart.objects.get_or_create(user=request.user)[0]
    cart_items = CartItem.objects.filter(cart=cart).select_related('product')
    return render(request, 'cart.html', {'cart': cart, 'cart_items': cart_items})



def add_to_cart(request, product_id):
    cart = Cart.objects.get_or_create(user=request.user)[0]
    product = Product.objects.get(id=product_id)
    
    # Get the source from the request data, if provided
    source = request.GET.get('source', 'manual')
    
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    
    cart_item.source = source
    cart_item.save()
    
    cart_items = CartItem.objects.filter(cart=cart).select_related('product')
    
    for item in cart_items:
        print(f"DEBUG: Quantity: {item.quantity}")
        print(f"DEBUG: Source: {item.source}")
    
    return render(request, 'cart.html', {'cart': cart, 'cart_items': cart_items})


def remove_from_cart(request, cart_item_id):
    cart_item = CartItem.objects.get(id=cart_item_id)
    cart_item.delete()
    return redirect('cart')
