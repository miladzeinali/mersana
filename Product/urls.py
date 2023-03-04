from django.urls import path
from .views import Products

app_name = 'product'
urlpatterns = [
    path('/products/',Products,name=products)
    path('/detailproduct/<int:id>/',ProductDetail,name=products)
]
