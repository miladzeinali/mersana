from django.shortcuts import render,redirect
from .models import *
from Product.models import Product
from django.contrib.messages.views import messages
from random import randint
import requests
from django.contrib.auth import login,logout
from django.contrib.auth.models import User
import time

def UserVerify(request):
        # try:
            mobile = request.session['r']['mobile']
            code = request.session['code']
            if mobile:
                # try:
                    print(mobile)
                    ValidationCode.objects.get(mobile=mobile,validation_code=code)
                    print('69')
                    user = User.objects.create(username=mobile,password=code)
                    print('71')
                    Userprofile.objects.create(mobile=mobile,user = user)
                    print('73')
                    user.save()
                    print('75')
                    login(request,user)
                    print('77')
                    messages.success(request,'به مرسانا خوش آمدید!','success')
                    return redirect('web:dashbord')
                # except:
                #     return redirect('account:userverify')
            else:
                messages.error(request,'مشکلی در فرآیند ثبت نام پیش آمده است!','error')
                return redirect('account:register')
        # except:
        #     messages.error(request, 'مشکلی در فرآیند ثبت نام پیش آمده است!', 'error')
        #     return redirect('account:register')

def UserForgetPass(request):
    if request.method == 'POST':
        form = request.POST
        if form['mobile']:
            try:
                mobile = form['mobile']
                rule = re.compile(r'(^0)[\d]{10}$')
                if not rule.search(form['mobile']):
                    messages.error(request, 'شماره موبایل معتبر نیست!', 'error')
                    return redirect('account:forgetpass')
                User.objects.get(username=mobile)
                code = ValidationCode.objects.get(mobile=mobile).validation_code
                print(code)
                r = {
                    'mobile': mobile,
                }
                resp = []
                resp.insert(0, r)
                request.session['r'] = r

                # send code for sms
                params = (('receptor', f'{mobile}'), ('token', f'{code}'), ('template', 'SendCode'))
                requests.post(
                    'https://api.kavenegar.com/v1/7335726878564E2F506C4A3857457773624F70634C466A7A586F456D345A78544F7845446B3263635832773D/verify/lookup.json',
                    params=params)
                return redirect('account:userverify')
            except:
                messages.error(request,'کاربری با این شماره ثیت نشده است!','error')
                return redirect('account:forgetpass')
        else:
            messages.error(request,'لطفا شماره موبایل را وارد نمایید!','error')
            return redirect('account:forgetpass')
    else:
        return render(request,'forgetpass.html')


def Userregister(request):
    if request.method == 'POST':
        form = request.POST
        if form['mobile']:
                        mobile = form['mobile']
                # try:
                    # try:
                        ValidOqbject = ValidationCode.objects.get(mobile=mobile)
                        code = ValidOqbject.validation_code
                        # send code to user
                        # params = (('receptor',f'{mobile}'),('token',f'{code}'),('template','sendmersana'))
                        # requests.post('https://api.kavenegar.com/v1/7335726878564E2F506C4A3857457773624F70634C466A7A586F456D345A78544F7845446B3263635832773D/verify/lookup.json',
                        #               params = params)
                        r = {
                            'mobile': mobile,
                            'code': code,
                        }
                        request.session['r'] = r
                        print(code)
                        return render(request,'userverify.html')
                    # except:
                    #     code = randint(100000,999999)
                    #     ValidationCode.objects.create(mobile=mobile,validation_code=code)
                        # send sms to user
                        # params = (('receptor', f'{mobile}'), ('token', f'{code}'), ('template', 'sendmersana'))
                        # requests.post('https://api.kavenegar.com/v1/7335726878564E2F506C4A3857457773624F70634C466A7A586F456D345A78544F7845446B3263635832773D/verify/lookup.json',
                        #               params = params)
                        # r = {
                        #     'mobile': mobile,
                        #     'code': code,
                        # }
                        # resp = []
                        # resp.insert(0, r)
                        # request.session['r'] = r
                        # print(code)
                        # return render(request,'userverify.html')
                # except:
                #     messages.error(request,'در فرآیند ثبت نام مشکلی پیش آمده است، با پشتیبانی سایت تماس بگیرید','error')
                #       return render(request,'register.html')
    else:
        return render(request,'login.html')

def UserVerify(request):
        try:
            mobile = request.session['r']['mobile']
            code = request.session['r']['code']
            if mobile:
                try:
                    try:
                        mobile = ValidationCode.objects.get(mobile=mobile,validation_code=code)
                        user = Userprofile.objects.get(mobile=mobile.mobile)
                        login(request,user.user)

                        return redirect('web:dashbord')
                    except:
                        ValidationCode.objects.get(mobile=mobile,validation_code=code)
                        user = User.objects.create(username=mobile,password=str(code))
                        Userprofile.objects.create(mobile=mobile,user = user)
                        user.save()
                        login(request,user)
                        messages.success(request,'به مرسانا خوش آمدید!','success')
                        return redirect('web:dashbord')
                except:
                    return redirect('web:home')
            else:
                messages.error(request,'مشکلی در فرآیند ثبت نام پیش آمده است!','error')
                return redirect('web:home')
        except:
            messages.error(request, 'مشکلی در فرآیند ثبت نام پیش آمده است!', 'error')
            return redirect('web:dashbord')

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
            return redirect('account:login')

def UserLogout(request):
    logout(request)
    messages.success(request, "شما با موفقیت خارج شدید!", 'success')
    return redirect('account:home')

