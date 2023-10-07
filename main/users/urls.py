from django.urls import path 
from .views import register_page, login_page, logout_request

urlpatterns = [
    path('register_user/', register_page, name='register_page'), 
    path('login_user/', login_page, name='login_page'),
    path('logout/', logout_request, name='logout_request')
]