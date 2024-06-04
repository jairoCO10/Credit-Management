from django.shortcuts import render

# Create your views here.
from rest_framework import status

from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from  Customers.models import Customers
from .Serializers import CustomersSerializer

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def customer(request: Request):
    """
    Obtener todos los clientes o crear uno nuevo.
    """
    
    customers = Customers.objects.all()
    serializer = CustomersSerializer(customers, many=True)
    return Response(serializer.data)
    

@api_view(['POST']) 
@permission_classes([IsAuthenticated])
def create_customer(request: Request):
    """
    Crea un nuevo cliente.
    """
    serializer = CustomersSerializer(data=request.data)
    try:
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    except Exception as e:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    

# Implementar las vistas y funciones para los demás servicios requeridos.
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_customer_balance(request, external_id):
    try:
        customer = Customers.objects.get(external_id=external_id)
    except Customers.DoesNotExist:
        return Response({"error": "Customer not found"}, status=status.HTTP_404_NOT_FOUND)
    
    total_debt = sum(loan.outstanding for loan in customer.loans.filter(status__in=[1, 2, 3]))
    available_amount = customer.score - total_debt
    
    data = {
        'external_id': customer.external_id,
        'score': customer.score,
        'available_amount': available_amount,
        'total_debt': total_debt
    }
    
    return Response(data)
