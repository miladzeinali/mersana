from django.shortcuts import render,redirect
from .models import Favorits,ValidationCode
from Product.models import Product
from django.contrib.messages.views import messages
from random import randint
import requests

def Userregister(request):
    if request.method == 'POST':
        form = request.POST
        print(form)
        if form['mobile']:
            mobile = form['mobile']
            print(mobile)
            try:
                Userprofile.objects.get(mobile=mobile)
                messages.error(request,'این شماره قبلا در سامانه ثبت شده است!','error')
                return render(request,'register.html')
            except:
                try:
                    # try:
                    #     ValidOqbject = ValidationCode.objects.get(mobile=mobile)
                    #     code = ValidOqbject.validation_code
                        # send code to user
                        # print('23')
                        # params = (('receptor',f'{mobile}'),('token',f'{code}'),('template','SendCode'))
                        # print('25')
                        #
                        # requests.post('https://api.kavenegar.com/v1/7335726878564E2F506C4A3857457773624F70634C466A7A586F456D345A78544F7845446B3263635832773D/verify/lookup.json',
                        #               params = params)
                        # print('29')
                        #
                        # r = {
                        #     'mobile': mobile,
                        # }
                        # print('34')
                        #
                        # resp = []
                        # resp.insert(0, r)
                        # request.session['r'] = r
                        # print(code)
                        # return render(request,'userverify.html')
                    # except:
                        print('42')
                        code = randint(100000,999999)
                        ValidationCode.objects.create(mobile=mobile,validation_code=code)
                        print('45')
                        # send sms to user
                        params = (('receptor', f'{mobile}'), ('token', f'{code}'), ('template', 'SendCode'))
                        requests.post('https://api.kavenegar.com/v1/7335726878564E2F506C4A3857457773624F70634C466A7A586F456D345A78544F7845446B3263635832773D/verify/lookup.json',
                                      params = params)
                        print('50')
                        r = {
                            'mobile': mobile,
                        }
                        resp = []
                        resp.insert(0, r)
                        request.session['r'] = r
                        print(code)
                        return render(request,'userverify.html')
                except:
                    messages.error(request,'در فرآیند ثبت نام مشکلی پیش آمده است، با پشتیبانی سایت تماس بگیرید','error')
                    return render(request,'register.html')
        else:
            return redirect('web:register')
    else:
        return render(request,'register.html')

def UserVerify(request):
        try:
            mobile = request.session['r']['mobile']
            code = request.POST['code']
            if mobile:
                try:
                    ValidationCode.objects.get(mobile=mobile,validation_code=code)
                    user = User.objects.create_user(username=mobile,password=code)
                    Userprofile.objects.create(father_phone=mobile,user = user)
                    user.save()
                    login(request,user)
                    messages.success(request,'به مرسانا خوش آمدید!','success')
                    return redirect('web:dashbord')
                except:
                    if form['next']:
                        next = form['next']
                        messages.error(request,'رمز را به صورت صحیح وارد نمایید!','error')
                        return redirect(next)
                    else:
                        return redirect('web:home')
            else:
                messages.error(request,'مشکلی در فرآیند ثبت نام پیش آمده است!','error')
                return redirect('web:home')
        except:
            messages.error(request, 'مشکلی در فرآیند ثبت نام پیش آمده است!', 'error')
            return redirect('web:home')

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

def UserLogin(request):
    if request.method == "POST":
        try:
            mobile = request.POST['mobile']
            password = request.POST['password']
            try:
                profile = Userprofile.objects.get(father_phone=mobile)
                user = profile.user
                userLogin = authenticate(request,username = mobile,password = password)
                if userLogin is not None:
                    login(request,user)
                    user.last_login = datetime.datetime.now()
                    user.save()
                    if profile.name:
                        messages.success(request,f' عزیز شما با موفقیت وارد شدید!{profile.name}','success')
                    else:
                        messages.success(request,'شما با موفقیت وارد شدید!','success')
                    return redirect('account:dashbord')
                else:
                    messages.error(request,'لطفا رمز را به صورت صحیح وارد کنید!','error')
                    return render(request,'login.html')
            except:
                messages.error(request,'نوآموزی با این شماره موبایل ثبت نام نشده است!','error')
                return render(request,'login.html')
        except:
            messages.error(request,'لطفا مقادیر را به صورت صحیح وارد نمایید!','error')
            return render(request,'login.html')
    else:
        return render(request,'login.html')


def UserLogout(request):
    logout(request)
    messages.success(request, "شما با موفقیت خارج شدید!", 'success')
    return redirect('account:home')

