from django.shortcuts import render
from seller.models import SellerProfile
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
# Create your views here.


def sellers_forms(request):
    sellers = SellerProfile.objects.all()
    return render(request, 'admin_panel.html', {'sellers':sellers})



def details(requset, seller_id):
    seller = SellerProfile.objects.get(id=seller_id)
    return render(requset, 'seller_detail.html', {'seller':seller})



def send_email_to_user(user):
    subject = 'Test Subject'
    html_message = render_to_string('send_email.html', {'user': user})
    plain_message = strip_tags(html_message) 

    # Send the email
    send_mail(subject, plain_message, 'testdjangoemail@gmail.com', [user.email], html_message=html_message)