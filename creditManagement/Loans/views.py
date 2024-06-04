from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from Loans.models import Loan
from  Customers.models import Customers
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

        **Responses:**
        - **201:**
            - **Description:** Préstamo creado exitosamente.
        - **400:**
            - **Description:** Error en la solicitud.
    """
    
    serializer = LoanSerializer(data=request.data)
    if serializer.is_valid():
        # Implementar lógica para validar el límite de crédito del cliente
        serializer.save(status=1)  # Set status to pending
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
@permission_classes([IsAuthenticated])
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
@permission_classes([IsAuthenticated])
def get_loans_by_customer(request, customer_external_id):
    """
        Obtener los préstamos de un cliente.

        ---

        **Parameters:**
        - `customer_external_id`:
            - **Description:** ID externo del cliente.
            - **Required:** true
            - **Type:** string

        **Responses:**
        - **200:**
            - **Description:** Retorna una lista de los préstamos del cliente.
        - **404:**
            - **Description:** Préstamos no encontrados para este cliente.
    """
    try:
        loans = Loan.objects.filter(customer_external_id=customer_external_id)
        
    except Loan.DoesNotExist:
        return Response({"error": "Loans not found for this customer"}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = LoanSerializer(loans, many=True)
    return Response(serializer.data)
