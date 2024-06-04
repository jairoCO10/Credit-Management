from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Customers


@admin.register(Customers)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['id', 'created_at', 'updated_at', 'external_id', 'status', 'score', 'preapproved_at']
