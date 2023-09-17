from django.urls import path 
from .views import sellers_forms


urlpatterns = [
    path('', sellers_forms)
]