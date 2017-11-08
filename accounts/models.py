from django.db import models
from customers.models import Customer

class CheckingAccount(models.Model):
    customer_id = models.ForeignKey(Customer)
    
    def __str__(self):
        return str(self.customer_id)

class SavingAccount(models.Model):
    customer_id = models.ForeignKey(Customer)

