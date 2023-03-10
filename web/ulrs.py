from django.urls import path
from .views import *
from Product.views import *

app_name = 'web'
urlpatterns = [
    path('', Home, name='home'),
    path('dashbord/',Dashbord,name='dashbord'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),

]
