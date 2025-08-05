from django.db import models

# Create your models here.

class Product(models.Model):
    title= models.CharField(max_length=200) # This becomes VARCHAR(200)
    price = models.PositiveIntegerField()  # This becomes INT with check value >=0
    desc = models.TextField(max_length=500, null=True)
    image = models.ImageField(upload_to='products/', null=True)

    def __str__(self):
      return f"Proudct : {self.title} for Rs. {self.price}."