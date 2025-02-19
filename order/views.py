from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Order, OrderBook, OrderClothes
from cart.models import Cart
from customer.models import Customer
from payment.models import Payment
from product.models import Book, Clothes

def confirm_order(request):
    """Display order confirmation page before proceeding to payment."""
    if not request.user.is_authenticated:
        return redirect('login')

    customer = get_object_or_404(Customer, user=request.user)
    cart = Cart.objects.filter(customer=customer).first()

    if not cart:
        messages.error(request, "Your cart is empty.")
        return redirect('cart_detail')

    cart_books = cart.cartbook_set.all()
    cart_clothes = cart.cartclothes_set.all()
    total_price = sum(item.book.price * item.quantity for item in cart_books) + \
                  sum(item.clothes.price * item.quantity for item in cart_clothes)

    return render(request, "confirm_order.html", {
        "cart_books": cart_books,
        "cart_clothes": cart_clothes,
        "total_price": total_price
    })


def payment_redirect(request):
    """Redirect the user to the payment app before order confirmation."""
    if not request.user.is_authenticated:
        return redirect('login')

    customer = get_object_or_404(Customer, user=request.user)
    cart = Cart.objects.filter(customer=customer).first()

    if not cart:
        messages.error(request, "Your cart is empty.")
        return redirect('cart_detail')

    cart_books = cart.cartbook_set.all()
    cart_clothes = cart.cartclothes_set.all()
    total_price = sum(item.book.price * item.quantity for item in cart_books) + \
                  sum(item.clothes.price * item.quantity for item in cart_clothes)
    order = Order.objects.create(customer=customer)
    for cart_book in cart_books:
            order_book = OrderBook.objects.create(order=order, book=cart_book.book, quantity=cart_book.quantity)
            order_book.save()
        # ✅ Link clothes to the order
    for cart_clothes_item in cart_clothes:
            order_clothes = OrderClothes.objects.create(order=order, clothes=cart_clothes_item.clothes, quantity=cart_clothes_item.quantity)
            order_clothes.save()
    # Redirect to external payment service
    payment_url = f"http://127.0.0.1:8000/payment/process/?amount={total_price}&order_id={order.id}&customer_id={customer.id}"
    
    return redirect(payment_url)


def create_order(request):
    """Create an order after successful payment."""
    if not request.user.is_authenticated:
        return redirect('login')

    customer = get_object_or_404(Customer, user=request.user)
    cart = get_object_or_404(Cart, customer=customer)

    # Ensure order is only created if payment is completed
    payment = Payment.objects.filter(customer=customer, status="completed").last()
    if not payment:
        messages.error(request, "Payment not completed. Please try again.")
        return redirect('confirm_order')

    # Create the order
    order = Order.objects.create()

    # Transfer books from cart to order
    cart_books = cart.cartbook_set.all()
    for item in cart_books:
        OrderBook.objects.create(order=order, book=item.book, quantity=item.quantity)

    # Transfer clothes from cart to order
    cart_clothes = cart.cartclothes_set.all()
    for item in cart_clothes:
        OrderClothes.objects.create(order=order, clothes=item.clothes, quantity=item.quantity)

    # Clear the cart
    cart.cartbook_set.all().delete()
    cart.cartclothes_set.all().delete()

    messages.success(request, "Order placed successfully!")
    return redirect('order_detail', order_id=order.id)


def order_detail(request, order_id):
    """Display order details."""
    order = get_object_or_404(Order, id=order_id)
    order_books = OrderBook.objects.filter(order=order)
    order_clothes = OrderClothes.objects.filter(order=order)

    return render(request, "order_detail.html", {
        "order": order,
        "order_books": order_books,
        "order_clothes": order_clothes
    })


def order_list(request):
    """List all orders of the logged-in customer."""
    if not request.user.is_authenticated:
        return redirect('login')

    customer = get_object_or_404(Customer, user=request.user)
    orders = Order.objects.filter(customer=customer).distinct() | \
             Order.objects.filter(customer=customer).distinct()

    return render(request, 'order_list.html', {'orders': orders})
