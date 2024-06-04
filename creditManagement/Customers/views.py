from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from  Customers.models import Customers
from Loans.models import Loan
from .Serializers import CustomersSerializer
from Loans.Serializers import LoanSerializer

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def customer(request: Request):
    """
    Obtener todos los clientes o crear uno nuevo.
    ---
    responses:
      200:
        description: Retorna una lista de todos los clientes.
    """
    customers = Customers.objects.all()
    serializer = CustomersSerializer(customers, many=True)
    return Response(serializer.data)

@api_view(['POST']) 
@permission_classes([IsAuthenticated])
def create_customer(request: Request):
    """
    Crea un nuevo cliente.
    ---
    parameters:
      - external_id: external_id
        description: identificador del cliente.
        required: true
        type: string
      - status: status
        description: estado de cliente.
        required: integer
        type: string
      - score: score
        description: Puntuancion del cliente.
        required: true
        type: decimal
      - preapproved_at: preapproved_at
        description: Valor preaprobado para el cliente.
        required: true
        type: datetime
    responses:
      201:
        description: Cliente creado exitosamente.
      400:
        description: Error en la solicitud.
    """
    serializer = CustomersSerializer(data=request.data)
    try:
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_customer_balance(request, customer_external_id):
    """
    Obtener los préstamos de un cliente.

    ---

    Parameters:
    - customer_external_id:
        Description: ID externo del cliente.
        Required: true
        Type: string

    Responses:
    - 200:
        Description: Retorna una lista de los préstamos del cliente.
    - 404:
        Description: Préstamos no encontrados para este cliente.
    """
    try:
        customer = Customers.objects.get(external_id=customer_external_id)
        loans = Loan.objects.filter(customer_id=customer)
    except Customers.DoesNotExist:
        return Response({"error": "Customer not found"}, status=status.HTTP_404_NOT_FOUND)
    except Loan.DoesNotExist:
        return Response({"error": "Loans not found for this customer"}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = LoanSerializer(loans, many=True)
    return Response(serializer.data)