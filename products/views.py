from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from .models import ProductCategory, Products
from .serializer import ProductCategorySerailizer, ProductSerializer
from common.authentication import JWTAuthentication
from common.permissions import IsAdminOrReadOnly, IsVendorOrReadOnly
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q

# Create your views here.

class ProductCategoryViewSet(ModelViewSet):

    permission_classes = [IsAdminOrReadOnly]
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerailizer



class ProductsView(ModelViewSet):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsVendorOrReadOnly]
    queryset = Products.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        serializer.save(vendor=self.request.user)

    def get_queryset(self):
        user = self.request.user

        if user.profile_type == "V":
            products = Products.objects.filter(vendor=user)
            return products
        return super().get_queryset()