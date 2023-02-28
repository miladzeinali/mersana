from django.contrib import admin
from .models import Userprofile,Address,ValidationCode
class UserprofileAdmin(admin.ModelAdmin):
    list_display = ('id','user','mobile','credit')
    search_fields = ('id','mobile','ssn')

class AddressAdmin(admin.ModelAdmin):
    list_display = ('id','user','city')
    search_fields = ('id','user')

class ValidationCodesAdmin(admin.ModelAdmin):
    list_display = ('id','mobile','validation_code')
    search_fields = ('id','mobile','validation_code')


admin.site.register(Userprofile,UserprofileAdmin)
admin.site.register(Address,AddressAdmin)
admin.site.register(ValidationCode,ValidationCodesAdmin)
