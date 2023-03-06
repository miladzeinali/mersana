from django.urls import path
from .views import *
from Product.views import *

app_name = 'web'
urlpatterns = [
    path('', Home, name='home'),
    # path('products/',Shop,name="products"),
    # path('webpaycontrol/',Webpaycontrol,name='webpaycontrol'),
    # path('payment/',Payment,name='payment'),
    path('dashbord/',Dashbord,name='dashbord'),
    # path('Info/',Info,name='info'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),

]
