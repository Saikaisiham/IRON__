from django.urls import path 
from .views import register_page, login_page

urlpatterns = [
    path('register_user/', register_page, name='register_page'), 
    path('login_user/', login_page, name='login_page')
]