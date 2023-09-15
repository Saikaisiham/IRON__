from django.db import models
from django.contrib.auth.models import User 
from django.core.exceptions import ValidationError

# Create your models here.

def cni_validator(value):
    if not(value.isupper() and len(value) == 8 and value[4:].isdigit()):
        raise ValidationError('Invalid CNI format')


class SellerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=150, blank=False, null=False)
    last_name = models.CharField(max_length=150, blank=False, null=False)
    cni = models.CharField(max_length=8, validators=[cni_validator])
    email = models.EmailField(unique=True, blank=False, null=False)
    image = models.ImageField(upload_to='seller/')
    address = models.TextField()
    phone_number = models.CharField(max_length=100, default='')





    def __str__(self):
        return f'{self.last_name} - {self.cni}'