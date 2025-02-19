from django.shortcuts import render, get_object_or_404
from product.models import Book, Clothes
from cart.models import Cart

def product_list_view(request):
    books = Book.objects.all()
    clothes = Clothes.objects.all()

    cart = None
    total_items = 0  # Corrected total items calculation

    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(customer=request.user.customer)
        total_items = sum(cart.cartbook_set.values_list("quantity", flat=True)) + \
                      sum(cart.cartclothes_set.values_list("quantity", flat=True))

    return render(request, "product_list.html", {"books": books, "clothes": clothes, "cart": cart, "total_items": total_items})

# View Book Detail
def book_detail_view(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, "book_detail.html", {"book": book})

# View Clothes Detail
def clothes_detail_view(request, clothes_id):
    clothes = get_object_or_404(Clothes, id=clothes_id)
    return render(request, "clothes_detail.html", {"clothes": clothes})