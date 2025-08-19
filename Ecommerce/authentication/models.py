from django.db import models

# Create your models here.
from django.contrib.auth.models import User

from django.utils import timezone
from datetime import timedelta

class EmailOTP(models.Model):
    email = models.EmailField()
    otp = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)

    def is_expired(self):
        return timezone.now() > self.created_at + timedelta(minutes=10)

    def __str__(self):
        return f"{self.email} - {self.otp}"
    

class Profile(models.Model):
    USER_TYPE = [
        ('buyer', 'Buyer'),
        ('seller', 'Seller'),
   
    ]

    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    user=models.OneToOneField (User,on_delete=models.CASCADE,related_name='user_profile')
    user_role=models.CharField(choices=USER_TYPE)
    profile_photo = models.ImageField(upload_to='profiles/', null=True, blank=True)  
    phone_number=models.PositiveIntegerField(null=True)
    address=models.TextField(null=True)
    email = models.EmailField(null = True)


    def __str__(self):
        return f"{self.user_role.capitalize()} Profile > {self.full_name}"

    @property
    def full_name(self):
        return f"{self.first_name.capitalize()} {self.last_name.capitalize()}"