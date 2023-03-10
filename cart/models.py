from django.db import models
from django.contrib.auth.models import User
from Product.models import Product

class Order(models.Model):
    STATUS_CHOICES = (
        ('Wpay', 'Wpay'),
        ('Processing', 'Processing'),
        ('Sended', 'Sended'),
        ('Delivered', 'Delivered'),
        ('Dispatched', 'Dispatched'),
        ('Canceled', 'Canceled')
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    province = models.CharField(max_length=50, null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    district = models.TextField(max_length=200, null=True, blank=True)
    code = models.CharField(max_length=35, null=True, blank=True)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(choices=STATUS_CHOICES, max_length=20, default='Wpay')

    class Meta:
        ordering = ('-created',)

    def get_total_quantity(self):
        return sum(item.quantity for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.FloatField(default=0)


class OrderManagement(models.Model):
    STATUS_CHOICES = (
        ('Wpay', 'Wpay'),
        ('Processing', 'Processing'),
        ('Sended', 'Sended'),
        ('Delivered', 'Delivered'),
        ('Dispatched', 'Dispatched'),
        ('Canceled', 'Canceled')
    )
    order = models.ForeignKey(Order, on_delete=models.CASCADE, default=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    province = models.CharField(max_length=50, null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    district = models.TextField(max_length=200, null=True, blank=True)
    code = models.CharField(max_length=40, null=True, blank=True)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=35, null=True, blank=True)
    last_name = models.CharField(max_length=35, null=True, blank=True)
    totalprice = models.CharField(max_length=35, null=True, blank=True)
    offprice = models.CharField(max_length=35, null=True, blank=True)
    offpercent = models.CharField(max_length=35, null=True, blank=True)
    sendcost = models.CharField(max_length=35, null=True, blank=True)
    count = models.CharField(max_length=10, null=True, blank=True)
    extramobile = models.CharField(max_length=11, null=True, blank=True)
    telephone = models.CharField(max_length=11, null=True, blank=True)
    tracking = models.CharField(max_length=50, null=True, blank=True)
    date = models.CharField(max_length=50,null=True,blank=True)
    time = models.CharField(max_length=50,null=True,blank=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(choices=STATUS_CHOICES, max_length=20, default='Wpay')
    tax = models.CharField(max_length=30,null=True,blank=True)
    explain = models.TextField(max_length=300,null=True,blank=True)


class Transaction(models.Model):
    choices = (('ci', 'cash_in'), ('co', 'cash_out'), ('tr', 'transfer'))
    first_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='firstuser')
    second_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    type = models.CharField(max_length=8, choices=choices)
    price = models.CharField(max_length=30)
    code = models.CharField(max_length=36, null=True, blank=True)
    description = models.TextField(null=True)
    date = models.DateTimeField(auto_now=True)

