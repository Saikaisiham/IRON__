from django.urls import path 
from .views import register, profile


urlpatterns = [
    path('',register),
    path('profile', profile)
]