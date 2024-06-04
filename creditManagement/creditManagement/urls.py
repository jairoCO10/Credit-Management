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

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', AuthViews.login, name='login'),
    path('create-user/', AuthViews.create_user, name='create_user'),
    path('customers/', CustomersViews.customer),
    path('create-customers/', CustomersViews.create_customer),
    path('customers/<str:external_id>/balance/', CustomersViews.get_customer_balance,),
    path('create-loans/', LoansViews.create_loan),
    path('loans/', LoansViews.getall_loan),
    path('loans/customer/<str:external_id>/', LoansViews.get_loans_by_customer),
    path('payments/', PaymentsViews.create_payment, name='create_payment'),
    path('payments/<str:external_id>/', PaymentsViews.get_payments_by_customer, name='payment_detail'),
    # path('customers/<str:customer_external_id>/payments/', PaymentsViews.get_payments_by_customer, name='payments_by_customer'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-doc'),
]
