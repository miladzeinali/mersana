from django.urls import path
from .views import *
from Product.views import *

app_name = 'web'
urlpatterns = [
    path('', Home, name='home'),
    path('products/',Shop,name="products"),
    path('register/',Userregister,name='register'),
    path('verify/',UserVerify,name='userverify'),
    path('forgetpass/',UserForgetPass,name='forgetpass'),

    # path('webpaycontrol/',Webpaycontrol,name='webpaycontrol'),
    # path('payment/',Payment,name='payment'),
    path('dashbord/',Dashbord,name='dashbord'),
    # path('Info/',Info,name='info'),

    path('logout/',UserLogout,name='logout'),
    path('login/',UserLogin,name='login'),

    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),

]
