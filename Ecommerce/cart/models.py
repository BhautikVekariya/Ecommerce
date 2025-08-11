from django.db import models
from django.contrib.auth.models import User
from mainapp.models import Product
# Create your models here.

class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def sub_total(self):
        return self.quantity * self.product.price 