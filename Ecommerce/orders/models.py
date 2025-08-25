from django.db import models

from django.contrib.auth.models import User
from mainapp.models import Product
from cart.models import CartItem
# Create your models here.

class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_address')
    line1 = models.CharField(max_length=100)
    line2 = models.CharField(max_length=100)
    category = models.CharField(choices = [
        ('Home','home'),
        ('Work', 'work'),
        ('Others', 'others')
    ], max_length=50)
    phno = models.CharField(max_length=12)
    pincode = models.PositiveIntegerField()




class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='order_user')
    total_amount = models.PositiveIntegerField()
    ordered_at = models.DateTimeField(auto_now_add=True)
    address = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True, blank=True)
    status = models.CharField(choices = [
        ('Pending', 'pending'),
        ('Completed', 'completed'),
        ('Cancelled', 'cancelled')
    ], default='Pending',
    max_length=20)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='order_product')
    quantity = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    price = models.PositiveIntegerField()

    @property
    def sub_total(self):
        return self.quantity * self.product.price 