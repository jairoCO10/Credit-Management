from django.contrib import admin

# Register your models here.
from .models import Payment


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['id', 'created_at', 'updated_at', 'external_id', 'total_amount', 'status', 'paid_at', 'customer']
