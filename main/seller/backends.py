from django.contrib.auth.backends import ModelBackend
from .models import SellerProfile

class EmailCNIAuthBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            seller_profile = SellerProfile.objects.get(email=username, cni=password)
            return seller_profile.user  
        except SellerProfile.DoesNotExist:
            return None  