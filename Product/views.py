from django.http import JsonResponse
from django.shortcuts import render,redirect
from .models import Product,Brand,Category,ProductImages
from account.models import Favorits
from cart.models import Order,OrderItem
from django.template.loader import render_to_string
from django.core.paginator import Paginator

def Products(request):
    products = Product.objects.all()
    orderitems = []
    countitems = []
    favorits = []
    total = 0
    countFave = []
    user = request.user
    countitems = len(orderitems)
    countFave = len(favorits)
    brands = Brand.objects.all()
    categorys = Category.objects.all()
    paginator = Paginator(products,9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    if user.is_authenticated:
        try:
            favorits = Favorits.objects.filter(user=user)
            countFave = len(favorits)
            try:
                order = Order.objects.get(user=user,status='Wpay')
                orderitems = OrderItem.objects.filter(order=order)
            except:
                pass
            countitems = len(orderitems)
            for item in orderitems:
                total += item.quantity*item.price
        except:
            pass
    return render(request,'products.html',{'products':page_obj,'orderitems':orderitems,'countfave':countFave,'countitems':countitems,
                                       'total':total,'brands':brands,'categorys':categorys})

def SaleProducts(request):
    products = Product.objects.filter(Sale = True)
    paginator = Paginator(products,9)
    orderitems = []
    countitems = []
    favorits = []
    total = 0
    countFave = []
    user = request.user
    countitems = len(orderitems)
    countFave = len(favorits)
    if user.is_authenticated:
        try:
            favorits = Favorits.objects.filter(user=user)
            countFave = len(favorits)
            try:
                order = Order.objects.get(user=user,status='Wpay')
                orderitems = OrderItem.objects.filter(order=order)
            except:
                pass
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
        orderitems = []
        countitems = []
        favorits = []
        total = 0
        countFave = []
        user = request.user
        countitems = len(orderitems)
        countFave = len(favorits)
        if product:
            try:
                try:
                    favorits = Favorits.objects.filter(user=user)
                    countFave = len(favorits)
                    order = Order.objects.get(user=user,status='Wpay')
                    orderitems = OrderItem.objects.filter(order=order)
                except:
                    pass
                countitems = len(orderitems)
                images = ProductImages.objects.filter(product=product)
                for item in orderitems:
                    total += item.quantity*item.price
            except:
                pass
        return render(request,'detail-product.html',{'product':product,'orderitems':orderitems,'countfave':countFave,'countitems':countitems,
                                       'total':total,'images':images})
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

def filter_data (request):
    categoris = request.GET.getlist('category[]')
    brands = request.GET.getlist('brand[]')
    genders = request.GET.getlist('gender[]')
    allProducts = Product.objects.all()
    if len(brands) > 0:
        allProducts = allProducts.filter(brand__Brand__in = brands).distinct()
    if len(categoris) > 0:
        allProducts = allProducts.filter(category__Category__in = categoris).distinct()
    if len(genders) > 0:
        print(genders)
        allProducts = allProducts.filter(gender__in = genders).distinct()
    t = render_to_string('ajax/product-list.html',{'data':allProducts})
    return JsonResponse({'data': t})
