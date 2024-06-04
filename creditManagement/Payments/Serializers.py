from Payments.models import Payment 
from rest_framework import serializers

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ['external_id', 'customer_id', 'loan_external_id', 'payment_date', 'status', 'total_amount', 'payment_amount']
        # extra_kwargs = {
        #     'external_id': {'required': True, 'error_messages': {'required': 'El external_id es obligatorio.'}},
        #     'customer_id': {'required': True, 'error_messages': {'required': 'El customer_id es obligatorio.'}},
        #     'loan_external_id': {'required': True, 'error_messages': {'required': 'El amount es obligatorio.'}},
        #     'payment_date': {'required': True, 'error_messages': {'required': 'El outstanding es obligatorio.'}},
        #     'status': {'required': True, 'error_messages': {'required': 'El status es obligatorio.'}},
        #     'total_amount': {'required': True, 'error_messages': {'required': 'El total_amount es obligatorio.'}},
        #     'payment_amount': {'required': True, 'error_messages': {'required': 'El payment_amount es obligatorio.'}},
        # }

