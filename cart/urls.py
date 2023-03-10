from django.urls import path
from .views.views import *
from .views.ordermange import checkout

app_name = 'cart'
urlpatterns = [
    path('ordercontrol/<str:code>/',OrderControl,name='ordercontrol'),
    path('updatecart/<int:id>/',OrderItemChange,name='orderchange'),
    path('deleteproduct/<int:id>/',OrderItemDelete,name='deleteitem'),
    
    path('checkout/',checkout,name='checkout'),
]