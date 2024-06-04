from django.db import models
from Customers.models import Customers

class Loan(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    external_id = models.CharField(max_length=60)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    status = models.CharField(max_length=50)
    contract_version = models.CharField(max_length=100)
    maximum_payment_date = models.DateField()
    taken_at = models.DateField()
    customer_id = models.ForeignKey(Customers, on_delete=models.CASCADE)
    outstanding = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return self.external_id
