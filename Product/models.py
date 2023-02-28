from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    Category = models.CharField(max_length=20)

    def __str__(self):
        return self.Category


class Brand(models.Model):
    Brand = models.CharField(max_length=20)
    BrandEnglish = models.CharField(max_length=20)

    def __str__(self):
        return self.Brand


class Color(models.Model):
    color = models.CharField(max_length=25)

    def __str__(self):
        return self.color


class Guarantee(models.Model):
    guarantee = models.CharField(max_length=200)
    guarantee_percent = models.CharField(max_length=10, null=True, blank=True, default='0')
    guarantee_price = models.CharField(max_length=20, null=True, blank=True, default='0')

    def __str__(self):
        return str(self.guarantee)


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    count = models.PositiveSmallIntegerField(default=0, null=True, blank=True)
    count_sell = models.PositiveSmallIntegerField(default=0, null=True, blank=True)
    code = models.CharField(max_length=15)
    title = models.CharField(max_length=150)
    image = models.ImageField(null=True, blank=True, upload_to='product-img/')
    price = models.FloatField(default=0)
    off_percent = models.IntegerField(default=0, null=True, blank=True)
    club_point = models.IntegerField(default=0, null=True, blank=True)
    color = models.ForeignKey(Color, on_delete=models.CASCADE, null=True, blank=True)
    guarantee = models.ForeignKey(Guarantee, on_delete=models.CASCADE)
    hashtag = models.TextField(max_length=60, null=True, blank=True)
    point = models.PositiveSmallIntegerField(default=0)
    Sale = models.BooleanField()
    sale_price = models.CharField(max_length=35, null=True, blank=True)
    date_created = models.DateField(auto_now=True)
    date_edited = models.DateField(auto_now=True)
    gender = models.BooleanField(default=False)
    locations = models.CharField(max_length=150,null=True,blank=True)
    season = models.CharField(max_length=150 ,null=True, blank=True)
    Fnote = models.CharField(max_length=250 ,null=True, blank=True)
    Mnote = models.CharField(max_length=250 ,null=True, blank=True)
    Lnote = models.CharField(max_length=250 ,null=True, blank=True)
    CountryMade = models.CharField(max_length=150 ,null=True, blank=True)
    YearMade = models.CharField(max_length=150 ,null=True, blank=True)
    Capacity = models.CharField(max_length=150 ,null=True, blank=True)
    gift = models.CharField(max_length=150 ,null=True, blank=True)

    def __str__(self):
        return str(self.title) + '-' + str(self.code)

class ProductImages(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE,default=1)
    img = models.ImageField(null=True, blank=True, upload_to='product-img/detail/')

class Transaction(models.Model):
    choices = (('ci', 'cash_in'), ('co', 'cash_out'), ('tr', 'transfer'))
    first_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='first_user')
    second_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='second_user')
    type = models.CharField(max_length=8, choices=choices)
    price = models.PositiveIntegerField()
    code = models.CharField(max_length=40, null=True, blank=True)
    description = models.TextField(null=True)
    date = models.DateTimeField(auto_now=True)

