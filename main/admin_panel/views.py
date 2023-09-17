from django.shortcuts import render
from seller.models import SellerProfile
# Create your views here.


def sellers_forms(request):
    sellers = SellerProfile.objects.all()
    return render(request, 'admin_panel.html', {'sellers':sellers})
