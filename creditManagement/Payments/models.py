# models.py
from django.db import models
from Customers.models import Customers
from Loans.models import Loan

class Payment(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    external_id = models.CharField(max_length=60)
    total_amount = models.DecimalField(max_digits=12, decimal_places=2)
    status = models.CharField(max_length=50)
    paid_at = models.DateField()
    customer = models.ForeignKey(Customers, on_delete=models.CASCADE)

    def __str__(self):
        return self.external_id

class PaymentLoanDetail(models.Model):
    id = models.AutoField(primary_key=True)
    payment = models.ForeignKey(Payment, related_name='payment_details', on_delete=models.CASCADE)
    loan = models.ForeignKey(Loan, on_delete=models.CASCADE)
    payment_amount = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return f"{self.payment.external_id} - {self.loan.external_id}"
