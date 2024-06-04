# views.py
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import Payment, PaymentLoanDetail
from Loans.models import Loan
from Customers.models import Customers
from .Serializers import PaymentSerializer


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_payment(request):
    """
    Crea un nuevo pago.

    ---

    **Parameters:**
    - `customer_external_id`:
        - **Description:** ID externo del cliente.
        - **Required:** true
        - **Type:** string
    - `total_amount`:
        - **Description:** Monto total del pago.
        - **Required:** true
        - **Type:** decimal
    - `loan_external_id`:
        - **Description:** ID externo del préstamo.
        - **Required:** true
        - **Type:** string
    - `payment_date`:
        - **Description:** Fecha del pago.
        - **Required:** true
        - **Type:** date
    - `payment_amount`:
        - **Description:** Monto del pago.
        - **Required:** true
        - **Type:** decimal

    **Responses:**
    - **201:**
        - **Description:** Pago creado exitosamente.
    - **400:**
        - **Description:** Error en la solicitud.
    """
    serializer = PaymentSerializer(data=request.data)
    if serializer.is_valid():
        # Obtener el cliente correspondiente al external_id proporcionado
        customer_external_id = request.data.get('customer_external_id')
        customer = get_object_or_404(Customers, external_id=customer_external_id)
        
        # Obtener el préstamo correspondiente al loan_external_id proporcionado
        loan_external_id = request.data.get('loan_external_id')
        loan = get_object_or_404(Loan, external_id=loan_external_id)
        
        total_amount = request.data.get('total_amount')
        payment_amount = request.data.get('payment_amount')
        
        if payment_amount <= 0:
            return Response({"error": "El monto del pago debe ser mayor que cero"}, status=status.HTTP_400_BAD_REQUEST)
        
        # Verificar que el cliente tenga préstamos activos y que el monto del pago no exceda la deuda
        if loan.customer_id == customer and loan.outstanding > 0 and payment_amount <= loan.outstanding:
            # Crear el pago
            payment = Payment.objects.create(
                total_amount=total_amount,
                status='completed',  # Se asume que el pago se crea como completado
                paid_at=request.data.get('payment_date'),
                customer=customer
            )
            
            # Crear el detalle del pago
            PaymentLoanDetail.objects.create(
                payment=payment,
                loan=loan,
                payment_amount=payment_amount
            )
            
            # Actualizar el monto pendiente del préstamo
            loan.outstanding -= payment_amount
            if loan.outstanding == 0:
                loan.status = 'paid'
            loan.save()
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({"error": "No se pueden aceptar pagos para este cliente o el monto del pago excede la deuda del préstamo"}, status=status.HTTP_400_BAD_REQUEST)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def get_payments_by_customer(request, external_id):
    """
    Obtener los pagos de un cliente.

    ---

    **Parameters:**
    - `external_id`:
        - **Description:** ID externo del cliente.
        - **Required:** true
        - **Type:** string

    **Responses:**
    - **200:**
        - **Description:** Retorna una lista de los pagos del cliente.
    - **404:**
        - **Description:** Pagos no encontrados para este cliente.
    """
    # Obtener el cliente correspondiente al external_id proporcionado
    customer = get_object_or_404(Customers, external_id=external_id)
    
    # Filtrar los pagos por el cliente obtenido
    payments = Payment.objects.filter(customer=customer)
    
    if payments.exists():
        serializer = PaymentSerializer(payments, many=True)
        return Response(serializer.data)
    
    return Response({"error": "Payments not found for this customer"}, status=status.HTTP_404_NOT_FOUND)
