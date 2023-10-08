from django.contrib import admin
from .models import Cart, CartItem, Favorite
# Register your models here.


admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Favorite)