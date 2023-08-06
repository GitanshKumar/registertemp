from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.CharField(max_length=255)
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    contact = models.CharField(max_length=14)



class Address(models.Model):
    street = models.CharField(max_length=100)
    landmark = models.CharField(max_length=100, null=True, blank=True)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    belongs_to = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="addresses")
