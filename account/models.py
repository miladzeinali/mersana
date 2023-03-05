from django.db import models
from django.contrib.auth.models import User

class Userprofile(models.Model):
    TYPE_CHOICE = (
        (1, 'کاربر معمولی'),
        (2, 'ادمین '),
    )
    type=models.PositiveSmallIntegerField(choices=TYPE_CHOICE,default=1)
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=1)
    gender = models.BooleanField(default=True)
    ssn = models.CharField(max_length=10, null=True, blank=True)
    mobile = models.CharField(max_length=11, default=0, unique=True)
    province = models.CharField(max_length=50, null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    county = models.CharField(max_length=50, null=True, blank=True)
    credit = models.IntegerField(default=0)
    def __str__(self):
        return f'{self.user} | {self.mobile}'

class Address(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    province=models.CharField(max_length=50)
    city=models.CharField(max_length=50)
    district = models.TextField(max_length=200)
    postcode=models.CharField(max_length=10)
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    def __str__(self):
        return f'{self.user}'

class ValidationCode(models.Model):
    mobile = models.CharField(max_length=11,null=True,blank=True)
    validation_code = models.CharField(max_length=5,null=True,blank=True)
    time_created = models.DateTimeField(null=True,blank=True)

class Favorits(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    code = models.CharField(max_length=20)