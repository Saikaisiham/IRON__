from django.urls import path
from .views import cart


urlpatterns = [
    path('add_to_cart/', cart, name='cart'),
]