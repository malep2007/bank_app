from django.db import models

class Bank(models.Model):
    bank_name = models.CharField(max_length=50)
    location = models.CharField(max_length=50, name='branch location')

    def __str__(self):
        return self.bank_name
