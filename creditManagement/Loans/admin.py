from django.contrib import admin

# Register your models here.
from .models import Loan


@admin.register(Loan)
class LoanAdmin(admin.ModelAdmin):
    list_display = ['id', 'created_at', 'updated_at', 'external_id', 'amount', 'status', 'contract_version', 'maximum_payment_date', 'taken_at', 'customer_id', 'outstanding']
    search_fields = ['external_id', 'status', 'contract_version']  # Agregar campos que se pueden buscar
    list_filter = ['status', 'contract_version']  # Agregar filtros
    readonly_fields = ['created_at', 'updated_at']  # Hacer que ciertos campos sean de solo lectura
    ordering = ['-created_at']  # Ordenar por fecha de creación descendente por defecto

    def get_readonly_fields(self, request, obj=None):
        if obj:  # Si está editando un registro existente, hacemos que el campo 'external_id' sea de solo lectura
            return self.readonly_fields + ['external_id']
        return self.readonly_fields

    # Personalizar el formulario de edición/agregado
    fieldsets = (
        (None, {
            'fields': ('external_id', 'amount', 'status')
        }),
        ('Date information', {
            'fields': ('contract_version', 'maximum_payment_date', 'taken_at'),
            'classes': ('collapse',)  # Ocultar este grupo por defecto
        }),
        ('Customer information', {
            'fields': ('customer_id', 'outstanding'),
            'classes': ('collapse',)  # Ocultar este grupo por defecto
        }),
    )

    # Habilitar la expansión de los grupos de campos en el formulario
    collapse_groups = True

