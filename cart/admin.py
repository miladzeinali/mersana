from django.contrib import admin
from .models import *

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id','user','status','city','code','postcode')
    search_fields = ('id','user','postcode','code','city')

class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('id','order','product','quantity')
    search_fields = ('id','product','quantity')

class OrderManagementsAdmin(admin.ModelAdmin):
    list_display = ('id','user','status','city','code','postcode')
    search_fields = ('id','user','postcode','code','city')

class TransactionsAdmin(admin.ModelAdmin):
    list_display = ('id','first_user','second_user','code','price')
    search_fields = ('id','first_user','code')




admin.site.register(Order,OrderAdmin)
admin.site.register(OrderItem,OrderItemAdmin)
admin.site.register(OrderManagement,OrderManagementsAdmin)
admin.site.register(Transaction,TransactionsAdmin)