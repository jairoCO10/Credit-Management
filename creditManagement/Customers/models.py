from django.db import models

# Create your models here.

class  Customers(models.Model):

    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    external_id = models.CharField(max_length=60)
    status =models.SmallIntegerField()
    score = models.DecimalField(max_digits=12, decimal_places=2)
    preapproved_at =models.DateTimeField(null=True, blank=True)


    def __str__(self) -> str:
        return self.external_id