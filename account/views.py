from django.shortcuts import render,redirect
from .models import *
from Product.models import Product
from django.contrib.messages.views import messages
from random import randint
import requests
from django.contrib.auth import login,logout
from django.contrib.auth.models import User
from cart.models import Order,OrderItem,OrderManagement
import re

def UserVerify(request):
        try:
            mobile = request.session['r']['mobile']
            code = request.session['code']
            if mobile:
                try:
                    print(mobile)
                    ValidationCode.objects.get(mobile=mobile,validation_code=code)
                    user = User.objects.create(username=mobile,password=code)
                    Userprofile.objects.create(mobile=mobile,user = user)
                    user.save()
                    login(request,user)
                    messages.success(request,'به مرسانا خوش آمدید!','success')
                    return redirect('web:dashbord')
                except:
                    return redirect('account:userverify')
            else:
                messages.error(request,'مشکلی در فرآیند ثبت نام پیش آمده است!','error')
                return redirect('account:register')
        except:
            messages.error(request, 'مشکلی در فرآیند ثبت نام پیش آمده است!', 'error')
            return redirect('account:register')


def Userregister(request):
    if request.method == 'POST':
        form = request.POST
        if form['mobile']:
                rule = re.compile(r'(^0)[\d]{10}$')
                if not rule.search(form['mobile']):
                    messages.error(request,'شماره موبایل معتبر نیست!','error')
                    return redirect('account:register')
                mobile = form['mobile']
                try:
                    try:
                        ValidOqbject = ValidationCode.objects.get(mobile=mobile)
                        code = ValidOqbject.validation_code
                        # send code to user
                        # params = (('receptor',f'{mobile}'),('token',f'{code}'),('template','sendmersana'))
                        # requests.post('https://api.kavenegar.com/v1/7335726878564E2F506C4A3857457773624F70634C466A7A586F456D345A78544F7845446B3263635832773D/verify/lookup.json',
                        #               params = params)
                        r = {
                            'mobile': mobile,
                        }
                        request.session['r'] = r
                        print(code)
                        return render(request,'userverify.html')
                    except:
                        code = randint(100000,999999)
                        ValidationCode.objects.create(mobile=mobile,validation_code=code)
                        # send sms to user
                        # params = (('receptor', f'{mobile}'), ('token', f'{code}'), ('template', 'sendmersana'))
                        # requests.post('https://api.kavenegar.com/v1/7335726878564E2F506C4A3857457773624F70634C466A7A586F456D345A78544F7845446B3263635832773D/verify/lookup.json',
                        #               params = params)
                        r = {
                            'mobile': mobile,
                        }
                        resp = []
                        resp.insert(0, r)
                        request.session['r'] = r
                        print(code)
                        return render(request,'userverify.html')
                except:
                    messages.error(request,'در فرآیند ثبت نام مشکلی پیش آمده است،   لطفا چند دقیقه دیگر امتحان کنید  ','error')
                    return render(request,'login.html')
    else:
        return render(request,'login.html')

def UserVerify(request):
        try:
            mobile = request.session['r']['mobile']
            code = request.POST['code']
            print(code)
            if mobile:
                try:
                    mobile = ValidationCode.objects.get(mobile=mobile,validation_code=code).mobile
                    try:
                        user = Userprofile.objects.get(mobile=mobile).user
                        login(request,user)
                        messages.success(request,'به مرسانا خوش آمدید!','success')
                        del request.session['r']
                        return redirect('web:home')
                    except:
                        user = User.objects.create_user(username=mobile,password=code)
                        Userprofile.objects.create(user=user,mobile=mobile)
                        user.save()
                        login(request,user)
                        del request.session['r']
                        return redirect('web:home')
                except:
                    messages.success(request,'رمز به صورت صحیح وارد نشده است !','error')
                    return redirect('account:register')
            else:
                messages.error(request,'مشکلی در فرآیند ثبت نام پیش آمده است!','error')
                return redirect('web:home')
        except:
            messages.error(request, 'مشکلی در فرآیند ثبت نام پیش آمده است!', 'error')
            return redirect('account:register')

def Favorit(request,code):
        user = request.user
        if user.is_authenticated:
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
        else:
            return redirect('account:register')
        
def deleteFavorits(request,code):
        user = request.user
        if user.is_authenticated:
            try:
                try:
                    favorit = Favorits.objects.get(user=user,code=code)
                    favorit.delete()
                except:
                    pass
                return redirect('account:favelist')
            except:
                pass
        else:
            return redirect('account:register')

def FavoriteReport(request):
        user = request.user
        if user.is_authenticated:
            try:
                products = []
                orderitems = []
                countitems = []
                total = 0
                countFave = []
                favorits = Favorits.objects.filter(user=user)
                for favorit in favorits:
                    product = Product.objects.get(code=favorit.code)
                    products.append(product)
                countFave = len(favorits)
                try:
                    order = Order.objects.get(user=user,status='Wpay')
                    orderitems = OrderItem.objects.filter(order=order)
                except:
                    pass
                countitems = len(orderitems)
                for item in orderitems:
                    total += item.quantity*item.price
                return render(request,'wishlist.html',{'products':products,'orderitems':orderitems,'countfave':countFave,'countitems':countitems,
                                       'total':total})            
            except:
                return redirect('product:products')
        else:
            return redirect('account:register')
    
def UserLogout(request):
    logout(request)
    messages.success(request, "شما با موفقیت خارج شدید!", 'success')
    return redirect('web:home')


def Dashboard(request):
    user = request.user
    ordermanages = []
    if user.is_authenticated:
        try:
            orders = Order.objects.filter(user=user,status='Wpay')
            for order in orders:
                ordermanage = OrderManagement.objects.filter(order=order)
                ordermanages.append(ordermanage)
        except:
            pass
        return render(request,'dashboard.html',{'ordermanages':ordermanages})

def DetailOrder(request):
    user = request.user
    if user.is_authenticated:
        pass