from django.urls import path
from . import views

urlpatterns = [
    path('cart/', views.cart_view, name='cart'),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<int:cart_item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('update_quantity/<int:cart_item_id>/', views.update_quantity, name='update_quantity'),
    path('add_remove_favorite/<int:product_id>/', views.add_remove_favorite, name='add_remove_favirote'),
    path('favorites/', views.favorite_products, name='favorite_products'),
]