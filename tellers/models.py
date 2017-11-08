from django.db import models

class Bank(models.Model):
    bank_name = models.CharField(max_length=50)
    location = models.CharField(max_length=50, name='branch location')

    def __str__(self):
        return self.bank_name
    
class Customer(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    address = models.CharField(max_length=50) 
    phone = models.CharField(max_length=10, name='phone number')
    account_no = models.CharField(max_length=50, name='account number')

    def __str__(self):
        return self.first_name + " " + self.last_name   

    def __unicode__(self):
        return 
