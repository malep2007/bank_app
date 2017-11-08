from django.contrib import admin
from . models import  Teller


# class BankAdmin(admin.ModelAdmin):
#     list_display = ('bank_name','branch location',)                     

# admin.site.register(Bank, BankAdmin)

class TellerAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','bank',)

admin.site.register(Teller, TellerAdmin)

# Register your models here.
