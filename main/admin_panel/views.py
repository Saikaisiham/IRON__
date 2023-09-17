from django.shortcuts import render
from seller.models import SellerProfile
# Create your views here.


def sellers_forms(request):
    sellers = SellerProfile.objects.all()
    return render(request, 'admin_panel.html', {'sellers':sellers})



def details(requset, seller_id):
    seller = SellerProfile.objects.get(id=seller_id)
    return render(requset, 'seller_detail.html', {'seller':seller})

