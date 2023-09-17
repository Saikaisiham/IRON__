from django.urls import path 
from .views import register, login_request

urlpatterns = [
    path('',register),
    path('login', login_request)
]