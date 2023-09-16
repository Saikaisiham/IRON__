from django.urls import path 
from .views import index, joinus


urlpatterns = [
    path('',index),
    path('joinus/', joinus)
]