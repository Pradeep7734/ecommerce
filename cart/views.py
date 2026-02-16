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

    def post(self, request):
        print("In views")
        serializer = CartSerializer(data=request.data, context={"request": request})
        print("Second views")
        if not serializer.is_valid():
            return Response(
                serializer.errors,
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
        
        print("11111")
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

