# from django.shortcuts import render
# from rest_framework.views import APIView
# from rest_framework.permissions import AllowAny
# from vendor.models import Products
# from .serializer import GetAllProductsSerializer
# from rest_framework.response import Response
# from rest_framework import status

# # Create your views here.

# class GetAllProductsView(APIView):
#     authentication_classes = []
#     permission_classes = [AllowAny]

#     def get(self, request, pk=None):
#         if pk:
#             try:
#                 product_obj = Products.objects.get(pk=pk)
#                 serializer = GetAllProductsSerializer(product_obj)
#                 return Response(serializer.data, status=status.HTTP_200_OK)
#             except Products.DoesNotExist:
#                 return Response({
#                     "message": "Product does not exists."
#                 }, status=status.HTTP_404_NOT_FOUND)
        
#         products = Products.objects.all()
#         serializer = GetAllProductsSerializer(products, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)

