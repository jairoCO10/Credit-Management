from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import Loan
from Customers.models import Customers
from .Serializers import LoanSerializer


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_loan(request):
    """
    Crea un nuevo préstamo.

    ---

    **Parameters:**
    - `customer_external_id`:
        - **Description:** ID externo del cliente.
        - **Required:** true
        - **Type:** string
    - `amount`:
        - **Description:** Monto del préstamo.
        - **Required:** true
        - **Type:** decimal
    - `outstanding`:
        - **Description:** Monto pendiente del préstamo.
        - **Required:** true
        - **Type:** decimal

    **Responses:**
    - **201:**
        - **Description:** Préstamo creado exitosamente.
    - **400:**
        - **Description:** Error en la solicitud.
    """
    
    serializer = LoanSerializer(data=request.data)
    if serializer.is_valid():
        # Obtener el cliente correspondiente al external_id proporcionado
        customer_external_id = request.data.get('customer_external_id')
        customer = get_object_or_404(Customers, external_id=customer_external_id)
        
        # Validar lógica de límite de crédito del cliente
        amount = request.data.get('amount')
        outstanding = request.data.get('outstanding')
        
        if customer.score - outstanding >= amount:
            # Crear el préstamo con estado activo (status=2)
            serializer.save(customer_id=customer, status=2)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({"error": "El monto del préstamo excede el límite de crédito del cliente"}, status=status.HTTP_400_BAD_REQUEST)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def getall_loan(request):
    """
    Obtener todos los préstamos.

    ---

    **Responses:**
    - **200:**
        - **Description:** Retorna una lista de todos los préstamos.
    """
    loans = Loan.objects.all()
    serializer = LoanSerializer(loans, many=True)
    return Response(serializer.data)
    
@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def get_loans_by_customer(request, external_id):
    """
    Obtener los préstamos de un cliente.

    ---

    **Parameters:**
    - `external_id`:
        - **Description:** ID externo del cliente.
        - **Required:** true
        - **Type:** string

    **Responses:**
    - **200:**
        - **Description:** Retorna una lista de los préstamos del cliente.
    - **404:**
        - **Description:** Préstamos no encontrados para este cliente.
    """
    # Usamos get_object_or_404 para obtener el cliente por su external_id
    customer = get_object_or_404(Customers, external_id=external_id)
    
    # Luego, filtramos los préstamos por el cliente obtenido
    loans = Loan.objects.filter(customer_id=customer)
    
    if loans.exists():
        serializer = LoanSerializer(loans, many=True)
        return Response(serializer.data)
    
    return Response({"error": "Loans not found for this customer"}, status=status.HTTP_404_NOT_FOUND)
