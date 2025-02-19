from django.urls import path
from order.views import confirm_order, create_order, order_detail, order_list, payment_redirect

urlpatterns = [
    path("confirm-order/", confirm_order, name="confirm_order"),
    path("create-order/", create_order, name="create_order"),
    path("<int:order_id>/", order_detail, name="order_detail"),
    path('', order_list, name='order_list'),
    path('payment-redirect/', payment_redirect, name='payment_redirect'),
]
