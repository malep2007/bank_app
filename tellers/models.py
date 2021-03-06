from django.db import models
from banks.models import Bank

# class Bank(models.Model):
#     bank_name = models.CharField(max_length=50)
#     location = models.CharField(max_length=50, name='branch location')

#     def __str__(self):
#         return self.bank_name
    
class Teller(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    address = models.CharField(max_length=50) 
    phone = models.CharField(max_length=10, name='phone number')
    bank = models.ForeignKey(Bank)

    def __str__(self):
        return self.first_name + " " + self.last_name   

    def __unicode__(self):
        return 

