from django.urls import path 
from .views import index, joinus, search


urlpatterns = [
    path('',index),
    path('joinus/', joinus),
    path('search', search, name='search')
]