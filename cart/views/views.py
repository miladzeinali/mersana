from django.shortcuts import render,redirect
from django.contrib import messages
from web.models import *
from Product.models import *
from cart.models import *


def OrderControl(request,code):
    user = request.user
    try:
        order = Order.objects.get(user=user, status='Wpay')
        product = Product.objects.get(code=code)
        if product.count != 0 and product.count >= 1:
            price = product.price
            if product.Sale == True:
                price = product.sale_price
            try:
                orderitem = OrderItem.objects.get(order=order, product=product)
                if product.count > orderitem.quantity:
                    orderitem.quantity += 1
                    orderitem.save()
                else:
                    return render(request, 'detail-product.html', {'product': product})
            except:
                OrderItem.objects.create(order=order, product=product,
                                         quantity=1, price=price)
            return render(request,'detail-product.html',{'product':product})
        else:
            return render(request,'detail-product.html',{'product':product})
    except:
        product = Product.objects.get(code=code)
        if product.count != 0 and product.count >= 1:
            order = Order.objects.create(user=user, status='Wpay')
            OrderItem.objects.create(order=order, product=product, quantity=1)
            return render(request,'detail-product.html',{'product':product})
        else:
            return render(request,'detail-product.html',{'product':product})


def OrderItemChange(request,id):
    user = request.user
    qty = request.POST['qty']
    print(request.POST)
    try:
        order = Order.objects.get(user=user, status='Wpay')
        product = Product.objects.get(id=id)
        orderitem = OrderItem.objects.get(order=order, product=product)
        if orderitem.quantity == 1:
            orderitem.delete()
            try:
                OrderItem.objects.get(order=order)
            except:
                order.delete()
            return redirect('web:home')
        if product.count > orderitem.quantity:
            orderitem.quantity += qty
            if orderitem.quantity > product.count:
                return redirect('web:home')
            orderitem.save()
        return redirect(next,message = 'تعداد با موفقیت افزوده شد :)')
    except:
        return redirect('web:home')


def OrderItemDelete(request,id):
    user = request.user
    try:
        order = Order.objects.get(user=user, status='Wpay')
        product = Product.objects.get(id=id)
        orderitem = OrderItem.objects.get(order=order, product=product)
        orderitem.delete()
        product.count += orderitem.quantity
    except:
        pass
    return redirect('web:dashbord')
