import requests
from ..models import *

def OrderManage(request):
    user = request.user
    if user.is_authenticated:
    