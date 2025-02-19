from django.db import models
from customer.models import Customer
from product.models import Book, Clothes

# Intermediate model for storing book quantity in the cart
class CartBook(models.Model):
    cart = models.ForeignKey("Cart", on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)  # Quantity for books

    def __str__(self):
        return f"{self.quantity}x {self.book.title} in Cart {self.cart.id}"

# Intermediate model for storing clothes quantity in the cart
class CartClothes(models.Model):
    cart = models.ForeignKey("Cart", on_delete=models.CASCADE)
    clothes = models.ForeignKey(Clothes, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)  # Quantity for clothes

    def __str__(self):
        return f"{self.quantity}x {self.clothes.name} in Cart {self.cart.id}"

# Cart Model
class Cart(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    books = models.ManyToManyField(Book, through=CartBook, blank=True)
    clothes = models.ManyToManyField(Clothes, through=CartClothes, blank=True)

    def __str__(self):
        return f"Cart {self.id} for {self.customer.user.username}"
