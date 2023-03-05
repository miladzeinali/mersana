from django.shortcuts import render,redirect
from .models import Favorits
from Product.models import Product

def Favorit(request,code):
        user = request.user
        try:
            try:
                Favorits.objects.get(user=user,code=code)
            except:
                Favorits.objects.create(user=user,code=code)
                product = Product.objects.get(code=code)
            return render(request, 'detail-product.html', {'product': product})
        except:
            product = Product.objects.get(code=code)
            return render(request,'detail-product.html',{'product':product})
