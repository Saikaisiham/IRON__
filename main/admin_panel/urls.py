from django.urls import path 
from .views import sellers_forms, details

app_name = 'seller'

urlpatterns = [
    path('', sellers_forms),
    path('detail/<int:seller_id>/', details, name='seller_detail')
]