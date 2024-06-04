# serializers.py
from rest_framework import serializers
from .models import Payment, PaymentLoanDetail

class PaymentLoanDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentLoanDetail
        fields = ['loan', 'payment_amount']

class PaymentSerializer(serializers.ModelSerializer):
    payment_details = PaymentLoanDetailSerializer(many=True, read_only=True)

    class Meta:
        model = Payment
        fields = ['external_id', 'total_amount', 'status', 'paid_at', 'payment_details']
