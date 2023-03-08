# -*- coding: utf-8 -*-
# Github.com/Rasooll
from django.http import HttpResponse
from django.shortcuts import redirect
from zeep import Client
from django.contrib import messages
from account.views import Webpaycontrol

MERCHANT = 'bdae3de6-ef15-49e6-903b-34cc18e656cb'
client = Client('https://www.zarinpal.com/pg/services/WebGate/wsdl')
amount = 5000  # Toman / Required
description = "توضیحات مربوط به تراکنش را در این قسمت وارد کنید"  # Required
email = 'email@example.com'  # Optional
mobile = '09123456789'  # Optional
CallbackURL = 'http://127.0.0.1:8000/zarinpal/verify/' # Important: need to edit for realy server.



def send_request(request):
    result = client.service.PaymentRequest(MERCHANT, amount, description, email, mobile, CallbackURL)
    if result.Status == 100:
        return redirect('https://www.zarinpal.com/pg/StartPay/' + str(result.Authority))
    else:
        return HttpResponse('Error code: ' + str(result.Status))

def verify(request):
    if request.GET.get('Status') == 'OK':
        result = client.service.PaymentVerification(MERCHANT, request.GET['Authority'], amount)
        if result.Status == 100:
            Webpaycontrol(request)
            return redirect('web:dashbord')
        elif result.Status==101:
            Webpaycontrol(request)
            return redirect('web:dashbord')
        else:
            messages.error(request,'فرآیند پرداخت موفقیت آمیز نبود !','error')
            return redirect('web:dashbord')
    else:
        messages.error(request,'تراکنش توسط شما کنسل شد‌ !','error')
        return redirect('web:dashbord')

