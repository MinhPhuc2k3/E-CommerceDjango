from django.shortcuts import render, redirect, get_object_or_404
from .models import Order
from cart.models import Cart

from django.shortcuts import render, redirect, get_object_or_404
from .models import Order
from cart.models import Cart
from customer.models import Customer  # ✅ Import Customer model

from django.shortcuts import render, get_object_or_404
from .models import Cart
from customer.models import Customer

def confirm_order(request):
    user = request.user
    customer = get_object_or_404(Customer, user=user)
    cart = get_object_or_404(Cart, customer=customer)

    # Get cart items
    cart_books = cart.cartbook_set.all()
    cart_clothes = cart.cartclothes_set.all()

    # Calculate total price
    total_price = sum(item.book.price * item.quantity for item in cart_books) + \
                  sum(item.clothes.price * item.quantity for item in cart_clothes)

    context = {
        'cart': cart,
        'cart_books': cart_books,
        'cart_clothes': cart_clothes,
        'total_price': total_price
    }

    return render(request, 'confirm_order.html', context)

def create_order(request):
    """Create an order after user confirmation."""
    if request.method == "POST":
        customer = get_object_or_404(Customer, user=request.user)  # ✅ FIXED
        cart = get_object_or_404(Cart, customer=customer)  # ✅ FIXED

        # Delete any previous order for this cart to avoid duplicates
        Order.objects.filter(cart=cart).delete()

        # Create the new order
        order = Order.objects.create(cart=cart)

        return redirect("order_detail", order_id=order.id)

    return redirect("cart_detail")  # Redirect back if accessed incorrectly


def order_detail(request, order_id):
    """Display order details."""
    order = get_object_or_404(Order, id=order_id)
    return render(request, "order_detail.html", {"order": order})

def order_list(request):
    customer = Customer.objects.get(user=request.user)
    orders = Order.objects.filter(cart__customer=customer)

    return render(request, 'order_list.html', {'orders': orders})