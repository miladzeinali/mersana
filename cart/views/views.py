from django.shortcuts import render,redirect
from django.contrib import messages
from web.models import *
from Product.models import *
from cart.models import *
from django.http import JsonResponse


def OrderControl(request,code):
    user = request.user
    print(request.POST)
    form = request.POST
    product = Product.objects.get(code=code)
    if request.POST:
        variety = form['variety']
    else:
        variety = product.variety1
    if user.is_authenticated:
        if request.method == 'POST':
            product = Product.objects.get(code=code)
            if form['variety']:
                variety = form['variety']
            else:
                variety = product.variety1
        try:
            order = Order.objects.get(user=user, status='Wpay')
            if product.count != 0 and product.count >= 1:
                if variety == product.variety1:
                    price = product.variety1price
                elif variety == product.variety2:
                    price = product.variety2price
                elif variety == product.variety3:
                    price = product.variety3price
                elif variety == product.variety4:
                    price = product.variety4price
                elif variety == product.variety5:
                    price = product.variety5price
                if product.Sale == True:
                    price = price - (price*product.off_percent/100)
                try:
                    orderitem = OrderItem.objects.get(order=order, product=product,variety=variety)
                    if product.count > orderitem.quantity:
                        orderitem.quantity += 1
                        total = orderitem.quantity * float(price)
                        orderitem.total = total
                        orderitem.save()
                    else:
                        return render(request, 'detail-product.html', {'product': product})
                except:
                    OrderItem.objects.create(order=order, product=product,
                                            quantity=1, price=price,total=price,variety=variety)
                return render(request,'detail-product.html',{'product':product})
            else:
                return render(request,'detail-product.html',{'product':product})
        except:
            product = Product.objects.get(code=code)
            price = 0
            if product.count != 0 and product.count >= 1:
                order = Order.objects.create(user=user, status='Wpay')
                if product.count != 0 and product.count >= 1:
                    if variety == product.variety1:
                        price = product.variety1price
                    elif variety == product.variety2:
                        price = product.variety2price
                    elif variety == product.variety3:
                        price = product.variety3price
                    elif variety == product.variety4:
                        price = product.variety4price
                    elif variety == product.variety5:
                        price = product.variety5price
                    elif product.Sale == True:
                        price = price - (price * product.off_percent / 100)
                    OrderItem.objects.create(order=order, product=product, quantity=1,price=price,total=price,variety=variety)
                    return render(request,'detail-product.html',{'product':product})
            else:
                return redirect('product:products')
    else:
        return redirect('account:register')


def OrderItemChange(request,id):
    user = request.user
    print(request.POST)
    try:
        order = Order.objects.get(user=user, status='Wpay')
        product = Product.objects.get(id=id)
        price = Product.price
        if product.Sale:
            price = product.sale_price
        orderitem = OrderItem.objects.get(order=order, product=product)
        if orderitem.quantity == 1 and qty < 1:
            orderitem.delete()
            try:
                OrderItem.objects.get(order=order)
            except:
                order.delete()
            return redirect('web:dashbord')
        if product.count > orderitem.quantity:
            orderitem.quantity += qty
            orderitem.total = price*orderitem.quantity
            if orderitem.quantity > product.count:
                return redirect('web:dashbord')
            orderitem.save()
        return redirect('web:dashbord')
    except:
        return redirect('web:dashbord')


def OrderItemDelete(request,id):
    user = request.user
    try:
        Order.objects.get(user=user, status='Wpay')
        orderitem = OrderItem.objects.get(id=id)
        product = orderitem.product
        orderitem.delete()
        product.count += orderitem.quantity
        product.save()
    except:
        pass
    return redirect('web:dashbord')



