from django.urls import path
from .views import *

app_name ='account'
urlpatterns = [
    path('favorits/<str:code>/',Favorit,name='favorits'),
    path('register/', Userregister, name='register'),
    path('verify/', UserVerify, name='userverify'),
    path('forgetpass/', UserForgetPass, name='forgetpass'),
    # path('logout/', UserLogout, name='logout'),
    path('login/', UserLogin, name='login'),

]