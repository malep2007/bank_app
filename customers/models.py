from django.db import models

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
