from rest_framework import status
from rest_framework.response import Response
from rest_framework.request import Request
from Payments.models import Payment
from .Serializers import PaymentSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_payment(request: Request):
    """
        Crear un nuevo pago o obtener todos los pagos.

        Para crear un nuevo pago, envía los datos del pago en el cuerpo de la solicitud en formato JSON.

        Si la solicitud es exitosa, recibirás una respuesta con el código de estado HTTP 200 OK y los datos de los pagos en formato JSON.

        Para crear un pago exitosamente, asegúrate de enviar todos los campos requeridos:
        - external_id
        - customer_id
        - loan_external_id
        - payment_date
        - status
        - total_amount
        - payment_amount
        """
    serializer = PaymentSerializer(data=request.data)
    if serializer.is_valid():
        # Implementar lógica para validar que el pago no exceda la deuda del cliente
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def payment(request):
    """
    Para obtener todos los pagos, envía una solicitud GET sin parámetros.
    """
    
    # Implementar la lógica para obtener todos los pagos
    payments = Payment.objects.all()
    serializer = PaymentSerializer(payments, many=True)
    return Response(serializer.data)


   