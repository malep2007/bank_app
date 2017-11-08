from django.contrib import admin
from . models import Bank

class BankAdmin(admin.ModelAdmin):
    list_display = ('bank_name','branch location')

admin.site.register(Bank, BankAdmin)

# Register your models here.
