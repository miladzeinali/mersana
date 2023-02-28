from django.contrib import admin
from .models import *

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('Category',)
    search_fields = ('Category',)

class BrandAdmin(admin.ModelAdmin):
    list_display = ('id','Brand')
    search_fields = ('id','Brand')

class ColorAdmin(admin.ModelAdmin):
    list_display = ('id','color')
    search_fields = ('id','color')

class GuaranteeAdmin(admin.ModelAdmin):
    list_display = ('id','guarantee')
    search_fields = ('id','guarantee')

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','title','brand','code','count','count_sell')
    search_fields = ('brand','code')

class ProductImagesAdmin(admin.ModelAdmin):
    list_display = ('id','product')
    search_fields = ('id','product')

admin.site.register(Category,CategoryAdmin)
admin.site.register(Brand,BrandAdmin)
admin.site.register(Color,ColorAdmin)
admin.site.register(Guarantee,GuaranteeAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(ProductImages,ProductImagesAdmin)