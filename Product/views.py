from django.shortcuts import render,redirect
from .models import Product
from account.models import Favorits
from cart.models import Order,OrderItem

def Products(request):
    products = Product.objects.all()
    orderitems = []
    countitems = []
    total = 0
    countFave = []
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
    return render(request,'products.html',{'products':products,'orderitems':orderitems,'countfave':countFave,'countitems':countitems,
                                       'total':total})

def ProductDetail(request,id):
    try:
        product = Product.objects.get(id=id)
        return render(request,'detail-product.html',{'product':product})
    except:
        return redirect('web:home')

def GenMale(request):
    try:
        products = Product.objects.filter(gender=False)
        return render(request,'products.html',{'products':products})
    except:
        return redirect('web:home')

def GenFemale(request):
    try:
        products = Product.objects.filter(gender=True)
        return render(request,'products.html',{'products':products})
    except:
        return redirect('web:home')
