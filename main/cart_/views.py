from django.shortcuts import render, redirect
from .models import Cart, CartItem
from products.models import Product
from django.http import JsonResponse

def cart_view(request):
    cart = Cart.objects.get_or_create(user=request.user)[0]
    cart_items = CartItem.objects.filter(cart=cart).select_related('product')
    return render(request, 'cart.html', {'cart': cart, 'cart_items': cart_items})



def add_to_cart(request, product_id):
    cart = Cart.objects.get_or_create(user=request.user)[0]
    product = Product.objects.get(id=product_id)
    

    
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    

    cart_items = CartItem.objects.filter(cart=cart).select_related('product')
    

    
    return render(request, 'cart.html', {'cart': cart, 'cart_items': cart_items})


def remove_from_cart(request, cart_item_id):
    cart_item = CartItem.objects.get(id=cart_item_id)
    cart_item.delete()
    return redirect('cart')


def update_quantity(request, cart_item_id):
    if request.method == 'POST':
        try:
            new_quantity = int(request.POST.get('quantity'))
            cart_item = CartItem.objects.get(pk=cart_item_id)
            cart_item.quantity = new_quantity
            cart_item.save()
            return JsonResponse({'success': True})
        except Exception as e:
            return JsonResponse({'success': False, 'error_message': str(e)})
    return JsonResponse({'success': False, 'error_message': 'Invalid request method'})
