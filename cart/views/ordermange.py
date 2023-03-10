import requests
from ..models import *
from django.shortcuts import render,redirect


def checkout(request):
    return render(request,'checkout.html')