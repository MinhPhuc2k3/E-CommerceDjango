from django.db import models
from order.models import Order
# Create your models here.
class Shipment(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    tracking_number = models.CharField(max_length=100, unique=True)
    status = models.CharField(max_length=50, choices=[
        ('pending', 'Pending'),
        ('shipped', 'Shipped'),
        ('delivered', 'Delivered')
    ], default='pending')

    def __str__(self):
        return f"Shipment {self.tracking_number} - {self.status}"