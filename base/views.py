from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.serializers import Serializer
from django.contrib.auth.models import User
from .models import Customer, Address

@api_view(['POST'])
def register(request):
    email = request.data['email']
    first_name = request.data['first_name']
    last_name = request.data['last_name']
    contact = request.data['contact']
    password = request.data['password']
    street = request.data['street']
    state = request.data['state']
    country = request.data['country']

    user = User(email=email, password=password)
    user.save()
    customer = Customer(user=user, first_name=first_name, last_name=last_name, contact=contact)
    customer.save()
    add = Address(street=street, state=state, country=country, belongs_to=customer)
    add.save()
    
    return Response(request.data)

def login(request):
    pass