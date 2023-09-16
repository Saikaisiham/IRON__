from django.db import models
from categories.models import Category
from seller.models import SellerProfile
# Create your models here.

class Product(models.Model):
    owner = models.ForeignKey(SellerProfile, on_delete=models.CASCADE, default='')
    product_name = models.CharField(max_length=100, blank=False, default=None)
    description = models.TextField(blank=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=None)
    product_image = models.ImageField(upload_to='media/products', blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    current_price = models.FloatField()
    

    def __str__(self):
        return f"{self.product_name} - {self.current_price}"
    
