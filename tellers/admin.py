from django.contrib import admin
from . models import Bank, Customer


class BankAdmin(admin.ModelAdmin):
    list_display = ('bank_name','branch location',)                     

admin.site.register(Bank, BankAdmin)

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','account number',)

admin.site.register(Customer, CustomerAdmin)

# Register your models here.
