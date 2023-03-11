from django.urls import path
from .views import *
 
app_name ='account'
urlpatterns = [
    path('favorits/<str:code>/',Favorit,name='favorits'),
    path('register/', Userregister, name='register'),
    path('verify/', UserVerify, name='userverify'),
    path('logout/', UserLogout, name='logout'),
    path('favorits/', FavoriteReport, name='favelist'),
    path('deletefave/<str:code>/', deleteFavorits, name='deletefave'),
    
    path('dashboard/', Dashboard, name='dashboard'),
    path('detailorder/<int:id>/', DetailOrder, name='detailorder'),
    path('trackorder/<int:id>/', TrackingOrder, name='trackorder'),
]
