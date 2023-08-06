from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Customer, Address

class RegisterSerializer(serializers.Serializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField(max_length=64)
    contact = serializers.CharField(max_length=14)
    street = serializers.CharField(max_length=100)
    landmark = serializers.CharField(max_length=100, null=True, blank=True)
    state = serializers.CharField(max_length=100)
    country = serializers.CharField(max_length=100)
    belongs_to = serializers.ForeignKey(Customer, on_delete=models.CASCADE)