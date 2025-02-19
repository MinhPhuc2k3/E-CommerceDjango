from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .models import Cart, CartBook, CartClothes
from product.models import Book, Clothes

@login_required
def cart_detail(request):
    cart = Cart.objects.get(customer=request.user.customer)
    return render(request, "cart_detail.html", {"cart": cart})

@login_required
def add_book_to_cart(request, book_id):
    if request.method == "POST":
        quantity = int(request.POST.get("quantity", 1))
        if quantity < 1:
            return HttpResponseForbidden("Invalid quantity")

        cart, created = Cart.objects.get_or_create(customer=request.user.customer)
        book = get_object_or_404(Book, id=book_id)

        cart_book, created = CartBook.objects.get_or_create(cart=cart, book=book)
        cart_book.quantity += quantity
        cart_book.save()

    return redirect("cart_detail")

@login_required
def add_clothes_to_cart(request, clothes_id):
    if request.method == "POST":
        quantity = int(request.POST.get("quantity", 1))
        if quantity < 1:
            return HttpResponseForbidden("Invalid quantity")

        cart, created = Cart.objects.get_or_create(customer=request.user.customer)
        clothes = get_object_or_404(Clothes, id=clothes_id)

        cart_clothes, created = CartClothes.objects.get_or_create(cart=cart, clothes=clothes)
        cart_clothes.quantity += quantity
        cart_clothes.save()

    return redirect("cart_detail")

# Remove a book from the cart
@login_required
def remove_book_from_cart(request, book_id):
    cart = get_object_or_404(Cart, customer=request.user.customer)
    cart_book = get_object_or_404(CartBook, cart=cart, book_id=book_id)

    if request.method == "POST":
        cart_book.delete()

    return redirect("cart_detail")

# Remove clothes from the cart
@login_required
def remove_clothes_from_cart(request, clothes_id):
    cart = get_object_or_404(Cart, customer=request.user.customer)
    cart_clothes = get_object_or_404(CartClothes, cart=cart, clothes_id=clothes_id)

    if request.method == "POST":
        cart_clothes.delete()

    return redirect("cart_detail")

# Remove all items from the cart
@login_required
def clear_cart(request):
    cart = get_object_or_404(Cart, customer=request.user.customer)

    if request.method == "POST":
        cart.books.clear()
        cart.clothes.clear()
        CartBook.objects.filter(cart=cart).delete()
        CartClothes.objects.filter(cart=cart).delete()

    return redirect("cart_detail")