from django.urls import path
from payment.views import process_payment

urlpatterns = [
    path('process/', process_payment, name='process_payment'),
]