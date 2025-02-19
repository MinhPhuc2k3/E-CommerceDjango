from django.shortcuts import render, redirect
from django.contrib import messages
from payment.models import Payment
from order.models import Order
from cart.models import Cart
from customer.models import Customer
def process_payment(request):
    amount = request.GET.get("amount")
    order_id = request.GET.get("order_id")
    customer_id = request.GET.get("customer_id")
    if not amount or not order_id or not customer_id:
        messages.error(request, "Invalid payment request.")
        return redirect("order_list")

    order = Order.objects.get(id=order_id)
    customer = Customer.objects.get(id=customer_id)

    if request.method == "POST":
        payment_method = request.POST.get("payment_method")

        # 🟢 STEP 2: LINK PAYMENT TO ORDER
        payment = Payment.objects.create(
            customer=customer,
            order=order,  # Link the order
            payment_method=payment_method,
            status="completed"
        )

        # 🟢 STEP 3: UPDATE ORDER STATUS AFTER PAYMENT
        order.status = "confirmed"
        order.save()

        messages.success(request, "Payment successful! Your order has been confirmed.")
        return redirect("order_list")  # Redirect to order list after payment

    return render(request, "process_payment.html", {"amount": amount, "order": order})
