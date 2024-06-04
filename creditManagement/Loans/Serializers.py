from rest_framework import serializers
from .models import Loan 



class LoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loan
        fields = ['external_id', 'customer_id', 'amount', 'outstanding', 'status']

        # extra_kwargs = {
        #     'external_id': {'required': True, 'error_messages': {'required': 'El external_id es obligatorio.'}},
        #     'customer_id': {'required': True, 'error_messages': {'required': 'El customer_id es obligatorio.'}},
        #     'amount': {'required': True, 'error_messages': {'required': 'El amount es obligatorio.'}},
        #     'outstanding': {'required': True, 'error_messages': {'required': 'El outstanding es obligatorio.'}},
        #     'status': {'required': True, 'error_messages': {'required': 'El status es obligatorio.'}},

        # }

