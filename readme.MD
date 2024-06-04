# Sistema de Gestión de Créditos

Este proyecto es un Sistema de Gestión de Créditos desarrollado con Django y Django REST Framework.

## Descripción

El Sistema de Gestión de Créditos permite a los usuarios realizar operaciones relacionadas con clientes, préstamos y pagos. Proporciona una API RESTful para interactuar con estas entidades, lo que permite a los clientes acceder y manipular los datos de manera programática.

## Características

- Creación de clientes.
- Obtención del saldo de un cliente.
- Creación de préstamos.
- Obtención de préstamos de un cliente.
- Creación de pagos.
- Documentación de la API con Swagger (Redoc).

## Requisitos

- Python 3.x
- Django
- Django REST Framework
- Instalación de otros requisitos (listados en requirements.txt)

## Instalación

1. Clona el repositorio:

```bash
git clone https://github.com/jairoCO10/Credit-Management.git
```


2. Instala los paquetes requeridos:
```bash
pip install -r requirements.txt
```

3. Realiza las migraciones de la base de datos:

```bash
python manage.py migrate
```

4. Inicia el servidor de desarrollo:
```bash
python manage.py runserver
```

# Uso
 ## Puedes utilizar la API a través de las siguientes URLs:

Clientes: /customers/

Préstamos: /loans/

Pagos: /payments/


Documentación API (Swagger Redoc): /redoc/

Autenticación
La API utiliza autenticación basada en JWT (JSON Web Tokens). Para acceder a los endpoints protegidos, primero debes obtener un token JWT enviando una solicitud POST a /login/. Luego, incluye este token en el encabezado Authorization de tus solicitudes.

Ejemplo de solicitud de token:

```bash
curl -X POST -H "Content-Type: application/json" -d '{"username": "tu_usuario", "password": "tu_contraseña"}' http://localhost:8000/login/
```
