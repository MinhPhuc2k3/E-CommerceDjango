from django.db import models

# Base Product Model
class Product(models.Model):
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True  # Prevent Django from creating a separate Product table

# Book Model Inheriting from Product
class Book(Product):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    publisher = models.CharField(max_length=255, blank=True, null=True)
    publication_date = models.DateField(blank=True, null=True)
    isbn = models.CharField(max_length=13, unique=True)
    genre = models.CharField(max_length=100, blank=True, null=True)
    pages = models.PositiveIntegerField(blank=True, null=True)
    language = models.CharField(max_length=50, default="English")
    image = models.ImageField(upload_to="books/", blank=True, null=True)

    def __str__(self):
        return f"{self.title} by {self.author}"

# Clothes Model Inheriting from Product
class Clothes(Product):
    name = models.CharField(max_length=255)
    brand = models.CharField(max_length=255, blank=True, null=True)
    size = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    material = models.CharField(max_length=100, blank=True, null=True)
    gender = models.CharField(max_length=20, choices=[("Men", "Men"), ("Women", "Women"), ("Unisex", "Unisex")])
    image = models.ImageField(upload_to="clothes/", blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.size}, {self.color})"
