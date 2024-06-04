
from rest_framework import serializers
from Customers.models import Customers 



class CustomersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customers
        fields = ['external_id', 'status', 'score', 'preapproved_at']  # Aquí lista todos los campos que deseas incluir en la serialización
        
        # Puedes agregar los campos requeridos aquí:
        extra_kwargs = {
            'external_id': {'required': True, 'error_messages': {'required': 'El external_id es obligatorio.'}},
            'status': {'required': True, 'error_messages': {'required': 'El status es obligatorio.'}},
            'score': {'required': True, 'error_messages': {'required': 'El score es obligatorio.'}},
            'preapproved_at': {'required': True, 'error_messages': {'required': 'El preapproved_at es obligatorio.'}},
        }
