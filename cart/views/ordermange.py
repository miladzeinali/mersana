from ..models import *
from django.shortcuts import render,redirect
from account.models import *
import requests
import json
from zarinpal.views import *

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
    else:
        return redirect('account:register')

def ordertopay(request):
    user = request.user
    if request.method == 'POST':
        try:
            form = request.POST
            print(form)
            if user.is_authenticated and form['first_name'] :
                r = requests.get('https://api.keybit.ir/time/')
                resp = r.json()
                time = resp['time24']['full']['fa']
                date = resp['date']['full']['unofficial']['usual']['fa']
                season = resp['season']['name']
                order = Order.objects.get(user=user,status='Wpay')
                try:
                    oldorder = OrderManagement.objects.get(order=order,user=user)
                    oldorder.delete()
                except:
                    pass 
                OrderManagement.objects.create(order=order,user=user,province=form['province'],city=form['city'],status='Wpay',
                                            district=form['district'],postcode=form['postcode'],first_name=form['first_name'],last_name=form['last_name'],
                                            totalprice=form['totalprice'],tax=form['tax'],extramobile=form['extramobile'],telephone=form['telephone'],
                                            explain=form['explain'],time=time,date=date,email=form['email'],season=season)
                return redirect('zarinpal:request')
        except:
            return redirect('web:dashbord')
    else:
        return redirect('web:home')

def orderpayed(request):
    user = request.user
    if user.is_authenticated:
        try:
            ordermanage = OrderManagement.objects.get(user=user,status='Wpay')
            orderitems = OrderItem.objects.filter(order=ordermanage.order)
            for orderitem in orderitems:
                product = orderitem.product
                product.count = product.count - orderitem.quantity
                product.count_sell = product.count_sell + orderitem.quantity
                product.save()
            mobile = user
            # send sms to user
            params = (('receptor', f'{mobile}'), ('token', f'{ordermanage.first_name}'),('token2', f'{ordermanage.id}'), ('template', 'orderpayed'))
            requests.post('https://api.kavenegar.com/v1/7335726878564E2F506C4A3857457773624F70634C466A7A586F456D345A78544F7845446B3263635832773D/verify/lookup.json',
                                      params = params)
            ordermanage.status = 'Processing'
            ordermanage.order.status = 'Processing'
            ordermanage.order.save()
            ordermanage.save()
        except:
            return redirect('product:products')
        
    
                