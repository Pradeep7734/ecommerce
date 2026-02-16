from django.shortcuts import render
from rest_framework.views import APIView
from .models import ProductCategory, Products
from .serializer import ProductCategorySerailizer, ProductSerializer
from common.authentication import JWTAuthentication
from common.permissions import IsVendorOrReadOnly
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q

# Create your views here.

class ProductCategoryView(APIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsVendorOrReadOnly]

    def post(self, request):
        serializer = ProductCategorySerailizer(data=request.data, context={'request':request})

        if not serializer.is_valid():
            return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)
        
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    

    def delete(self, request, pk):
        try:
            category = ProductCategory.objects.get(pk=pk)
            category.delete()
            return Response(
                {
                    "message": f"{category.name} Deleted successfully."
                },
                status=status.HTTP_200_OK
            )
        except ProductCategory.DoesNotExist:
            return Response(
            {"error": "Category not found"},
            status=status.HTTP_404_NOT_FOUND
        )

    
    def get(self, request, pk=None):
        if pk:
            try:
                category = ProductCategory.objects.get(pk=pk)
                serializer = ProductCategorySerailizer(category)
                return Response(
                    serializer.data, status=status.HTTP_200_OK
                )
                
            except ProductCategory.DoesNotExist:
                return Response(
                    {
                        "message": "Category does not exists."
                    }, status=status.HTTP_400_BAD_REQUEST
                )
            
        else:
            categories = ProductCategory.objects.all()
            serializer = ProductCategorySerailizer(categories, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)



class ProductsView(APIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsVendorOrReadOnly]

    def post(self, request):

        serializer = ProductSerializer(data=request.data, context={"request":request})

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)
    

    def delete(self, request, pk):
        try:
            product = Products.objects.get(pk=pk)
            product.delete()
            return Response({
                "message": f"{product.name} deleted successfully."
            }, status=status.HTTP_200_OK)
        except Products.DoesNotExist:
            return Response({
                "message": "Product not found."
            }, status=status.HTTP_404_NOT_FOUND)
        
    
    def get(self, request, pk=None):
        if pk:
            try:
                product = Products.objects.get(pk=pk)
                serializer = ProductSerializer(product)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Products.DoesNotExist:
                return Response({
                "message": "Product not found."
            }, status=status.HTTP_404_NOT_FOUND)
        else:
            search = request.query_params.get("search")
            products = Products.objects.all()
            print(f"Products: {products}")

            if search:
                products = products.filter(
                    Q(name_icontains=search),
                    Q(description_icontains=search),
                    Q(category_name_icontains=search),
                )
            serializer = ProductSerializer(products, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)