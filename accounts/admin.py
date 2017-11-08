from django.contrib import admin
from . models import CheckingAccount, SavingAccount

class CheckingAccountAdmin(admin.ModelAdmin):
    list_display = ('customer_id',)

class SavingAccountAdmin(admin.ModelAdmin):
    list_display = ('customer_id',)

admin.site.register(SavingAccount, SavingAccountAdmin)


admin.site.register(CheckingAccount, CheckingAccountAdmin)
