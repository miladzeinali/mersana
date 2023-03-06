from django.urls import path
from .views.views import *

app_name = 'cart'
urlpatterns = [
    path('ordercontrol/<str:code>/',OrderControl,name='ordercontrol'),
    path('updatecart/',OrderItemChange,name='orderchange'),
    path('deleteproduct/<int:id>/',OrderItemDelete,name='deleteitem'),
]