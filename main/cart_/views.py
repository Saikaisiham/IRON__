from django.shortcuts import render, redirect
from .models import Cart, CartItem, Favorite
from products.models import Product
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required



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



@login_required
def add_remove_favorite(request, product_id):
    user = request.user
    if user.is_authenticated:
        try:
            favorite = Favorite.objects.get(user=user, product_id=product_id)
            favorite.delete()
        except Favorite.DoesNotExist:
            Favorite.objects.create(user=user, product_id=product_id)
        
        favorite_product_ids = user.favorite_set.values_list('product_id', flat=True)
        
        return render(request, 'product_detail.html', {'product_id': product_id, 'favorite_product_ids': favorite_product_ids})
    return redirect('/clients/login_user/')




def favorite_products(request):
    user = request.user
    if user.is_authenticated:
        favorite_products = Favorite.objects.filter(user=user)
        return render(request, 'favorites.html', {'favorite_products': favorite_products})
    return redirect('/clients/login_user/')