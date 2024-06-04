from django.contrib import admin
from django.urls import path
from rest_framework import routers
from Customers import views as CustomersViews
from Loans import views as LoansViews
from Payments import views as PaymentsViews
# from  creditManagement import views as AuthViews
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from . import views as AuthViews


router = routers.DefaultRouter()

schema_view = get_schema_view(
    openapi.Info(
        title="Credit Management",
        default_version='v1',
        description="Descripción de tu API",
    ),
    public=False,
)

# # Define el esquema para el cuerpo de la solicitud de cada endpoint
# create_customer_request_body = openapi.Schema(
#     type=openapi.TYPE_OBJECT,
#     properties={
#         'name': openapi.Schema(type=openapi.TYPE_STRING),
#         'email': openapi.Schema(type=openapi.TYPE_STRING),
#         # Añade más campos según sea necesario
#     },
#     required=['name', 'email']
# )

# create_loan_request_body = openapi.Schema(
#     type=openapi.TYPE_OBJECT,
#     properties={
#         'customer_id': openapi.Schema(type=openapi.TYPE_INTEGER),
#         'amount': openapi.Schema(type=openapi.TYPE_NUMBER),
#         # Añade más campos según sea necesario
#     },
#     required=['customer_id', 'amount']
# )

# create_payment_request_body = openapi.Schema(
#     type=openapi.TYPE_OBJECT,
#     properties={
#         'external_id': openapi.Schema(type=openapi.TYPE_STRING),
#         'customer_id': openapi.Schema(type=openapi.TYPE_INTEGER),
#         # Añade más campos según sea necesario
#     },
#     required=['external_id', 'customer_id']
# )

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', AuthViews.login, name='login'),
    path('create-user/', AuthViews.create_user, name='create_user'),
    path('customers/', CustomersViews.customer),
    path('create-customers/', CustomersViews.create_customer),
    path('customers/<str:external_id>/balance/', CustomersViews.get_customer_balance,),
    path('create-loans/', LoansViews.create_loan),
    path('loans/', LoansViews.getall_loan),
    path('create-payments/', PaymentsViews.create_payment),
    path('payments/', PaymentsViews.payment),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-doc'),
]
