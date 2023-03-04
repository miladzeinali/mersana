from django.shortcuts import render,redirect
from .models import Product

def Products(request):
    products = Product.objects.all()
    return render(request,'products.html',{'products':products})

def ProductDetail(request,id):
    try:
        product = Product.objects.get(id=id)
        return render(request,'detail-product.html',{'product':product})
    except:
        return redirect('web:home')
