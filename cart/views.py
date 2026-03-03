from django.shortcuts import render
from .models import Cart, CartItems
from products.models import Products
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import CartItemsSerializer
from common.permissions import IsCustomerOrVendor
from common.authentication import JWTAuthentication
import logging

logger = logging.getLogger(__name__)


# Create your views here.
class CartItemsView(APIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsCustomerOrVendor]

    def post(self, request):
        logger.info("CartItemsView post method called")
        logger.debug(f"Got request data: {request.data}")

        cart_item_serializer = CartItemsSerializer(data=request.data, context={'request':request})

        if not cart_item_serializer.is_valid():
            logger.warning("Serializer validation failed")
            return Response(cart_item_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        cart_item = cart_item_serializer.save()
        logger.debug(f"Cart item created successfully: {cart_item}")
        
        return Response(cart_item, status=status.HTTP_201_CREATED)






