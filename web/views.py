from django.shortcuts import render,redirect
from Product.models import *
from django.contrib import messages
from cart.models import Order,OrderItem
from account.models import Favorits,Userprofile
from django.contrib.auth.models import User

def Home(request):
    newest = Product.objects.all()
    orderitems = []
    countitems = []
    total = 0
    countFave = 0
    user = request.user
    if user.is_authenticated:
        try:
            favorits = Favorits.objects.filter(user=user)
            countFave = len(favorits)
            order = Order.objects.get(user=user,status='Wpay')
            orderitems = OrderItem.objects.filter(order=order)
            countitems = len(orderitems)
            for item in orderitems:
                total += item.quantity*item.price
        except:
            pass
    return render(request,'home.html',{'newest':newest,'orderitems':orderitems,'countfave':countFave,'countitems':countitems,
                                       'total':total})

def Shop(request):
    products = Product.objects.all()[0:4]
    return render(request,'products.html',{products:'products'})

def Dashbord(request):
    orderitems = []
    countitems = []
    total = 0
    countFave = 0
    user = request.user
    if user.is_authenticated:
        try:
            favorits = Favorits.objects.filter(user=user)
            countFave = len(favorits)
            order = Order.objects.get(user=user,status='Wpay')
            orderitems = OrderItem.objects.filter(order=order)
            countitems = len(orderitems)
            for item in orderitems:
                total += item.quantity*item.price
        except:
            pass
    return render(request,'cart.html',{'orderitems':orderitems,'countfave':countFave,'countitems':countitems,
                                       'total':total})

def about(request):
   return render(request,'about.html')

def contact(request):
    return render(request,'detail-product.html')
