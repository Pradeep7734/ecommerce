from django.shortcuts import render
from .models import Cart, CartItems
from products.models import Products
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import CartSerializer
from common.permissions import IsCustomer


# Create your views here.
class CartView(APIView):

    permission_classes = [IsCustomer]

