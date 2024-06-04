from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from django.shortcuts import render
from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view


from django.contrib.auth import authenticate
from django.http import JsonResponse

@api_view(['POST'])
def login(request):
    # Obtener las credenciales de inicio de sesión del cuerpo de la solicitud
    username = request.data.get('username')
    password = request.data.get('password')

    # Autenticar al usuario utilizando las credenciales proporcionadas
    user = authenticate(request, username=username, password=password)

    # Verificar si la autenticación fue exitosa
    if user is not None:
        # Si la autenticación fue exitosa, generar y devolver el token de acceso
        # Aquí puedes usar la lógica para generar el token JWT, como lo hiciste antes
        refresh = RefreshToken.for_user(user)
        return JsonResponse({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        })
    else:
        # Si la autenticación falló, devolver un mensaje de error
        return JsonResponse({'error': 'Credenciales inválidas'}, status=status.HTTP_401_UNAUTHORIZED)
    

@api_view(['POST'])
def create_user(request):
    
    username = request.data.get('username')
    password = request.data.get('password')
    email = request.data.get('email')

    if not username or not password or not email:
        return Response({'error': 'Se requieren campos obligatorios'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        user = User.objects.create_user(username=username, password=password, email=email)
        return Response({'success': 'Usuario creado correctamente'}, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response({'error': f'Error al crear usuario: {str(e)}'}, status=status.HTTP_400_BAD_REQUEST)
