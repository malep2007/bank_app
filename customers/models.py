from django.db import models
from banks.models import Bank
import uuid

class Customer(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    address = models.CharField(max_length=50) 
    phone = models.CharField(max_length=10, name='phone number')
    account_no = models.CharField(max_length=200, editable=False, name='account number', null=True)

    def __init__(self, *args, **kwargs):
        super(Customer,self).__init__()
        self.account_no = str(uuid.uuid4())
        
    
    def __str__(self):
        return self.first_name + " " + self.last_name   

    def __unicode__(self):
        return 
