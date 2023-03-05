from django.urls import path
from .views import *

app_name = 'product'
urlpatterns = [
    path('products/',Products,name='products'),
    path('detailproduct/<int:id>/',ProductDetail,name='product'),
    path('maleproducts/',GenMale,name='genmale'),
    path('femaleproducts/',GenFemale,name='genfemale'),
]
