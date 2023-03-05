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

def GenMale(request):
    try:
        products = Product.objects.filter(gender=False)
        return render(request,'GenMale.html',{'products':products})
    except:
        return redirect('web:home')

def GenFemale(request):
    try:
        products = Product.objects.filter(gender=True)
        return render(request,'GenFemale.html',{'products':products})
    except:
        return redirect('web:home')