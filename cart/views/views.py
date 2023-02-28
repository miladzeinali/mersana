from django.shortcuts import render,redirect
from django.contrib import messages.messages
from web.models import


def Products(request):




def OrderControl(self, request):
    user = request.user
    data = request.data
    code = data['code']
    qty = data['qty']
    if request.method == 'POST':
        next = request.POST['next']
    else:
        next = 'products.html'
    try:
        order = Order.objects.get(user=user, status='Wpay')
        product = Product.objects.get(code=code)
        if product.count != 0 and product.count >= qty:
            price = product.price
            if product.Sale == True:
                price = product.sale_price
            try:
                orderitem = OrderItem.objects.get(order=order, product=product)
                if product.count > orderitem.quantity:
                    orderitem.quantity += qty
                    orderitem.save()
                else:
                    return redirect(next,message = 'درخواست شما از موجودی بیشتر است :(')
            except:
                OrderItem.objects.create(order=order, product=product,
                                         quantity=qty, price=price)
            return redirect(next,message = 'محصول با موفقیت به سبد خرید اضافه شد :)')
        else:
            return redirect(next,message = 'موجودی به پایان رسیده است :(')
    except:
        product = Product.objects.get(code=code)
        if product.count != 0 and product.count >= qty:
            order = Order.objects.create(user=user, status='Wpay')
            OrderItem.objects.create(order=order, product=product, quantity=qty)
            return redirect(next,message = 'محصول با موفقیت به سبد خرید اضافه شد :)')
        else:
            return redirect(next,message = 'موجودی به پایان رسیده است :(')


def OrderItemChange(self, request):
    user = request.user
    code = request.data['code']
    qty = request.data['qty']
    if request.method == 'POST':
        next = request.POST['next']
    else:
        next = 'products.html'
    try:
        order = Order.objects.get(user=user, status='Wpay')
        product = Product.objects.get(code=code)
        orderitem = OrderItem.objects.get(order=order, product=product)
        if orderitem.quantity == 1 and qty < 1:
            orderitem.delete()
            try:
                OrderItem.objects.get(order=order)
            except:
                order.delete()
            return redirect(next,message = 'محصول از سبد خرید حذف شد :(')
        if product.count > orderitem.quantity:
            orderitem.quantity += qty
            if orderitem.quantity > product.count:
                return redirect(next,message = 'درخواست شما بیش از موجودی ماست :(')
            orderitem.save()
        return redirect(next,message = 'تعداد با موفقیت افزوده شد :)')
    except:
        return redirect('web:home',message = 'اشکال در فرایند، با پشتیبانی تماس بگیرید !')


def OrderItemDelete(self, request):
    user = request.user
    code = request.data['code']
    if request.method == 'POST':
        next = request.POST['next']
    else:
        next = 'products.html'
    try:
        order = Order.objects.get(user=user, status='Wpay')
        product = Product.objects.get(code=code)
        orderitem = OrderItem.objects.get(order=order, product=product)
        orderitem.delete()
        product.count += orderitem.quantity
        return redirect(next)
    except:
        return redirect(next)
