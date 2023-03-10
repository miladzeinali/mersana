from ..models import *
from django.shortcuts import render,redirect
from account.models import *

def checkout(request):        
    user = request.user
    if user.is_authenticated:
        orderitems = []
        countitems = []
        total = 0
        orderitems = []
        countFave = 0
        totaltax = 0
        tax = 0
        user = request.user
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
            tax = total*0.09
            totaltax = (total*0.09) + total
        else:
            return redirect('account:register')
    return render(request,'checkout.html',{'orderitems':orderitems,'countfave':countFave,'countitems':countitems,
                                       'total':total,'totaltax':totaltax,'tax':tax})
    

