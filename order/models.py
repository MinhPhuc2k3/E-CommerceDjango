from django.db import models
from cart.models import Cart
from product.models import Book, Clothes
from customer.models import Customer
class OrderBook(models.Model):
    order = models.ForeignKey("Order", on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)  # Quantity for books

    def __str__(self):
        return f"{self.quantity}x {self.book.title} in Cart {self.cart.id}"

# Intermediate model for storing clothes quantity in the cart
class OrderClothes(models.Model):
    order = models.ForeignKey("Order", on_delete=models.CASCADE)
    clothes = models.ForeignKey(Clothes, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)  # Quantity for clothes

    def __str__(self):
        return f"{self.quantity}x {self.clothes.name} in Cart {self.cart.id}"


# Create your models here.
class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.DO_NOTHING)
    books = models.ManyToManyField(Book, through=OrderBook, blank=True)
    clothes = models.ManyToManyField(Clothes, through=OrderClothes, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id} by {self.customer.username}"