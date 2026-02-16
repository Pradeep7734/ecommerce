from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import RegisterUserSerializer, RegisterVendorSerializer, LoginUserSerializer, LoginVendorSerializer
from rest_framework import status
from rest_framework.permissions import AllowAny

class RegisterUserView(APIView):
    authentication_classes = []
    permission_classes = [AllowAny]

    def post(self, request):
    
        serializer = RegisterUserSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.save(), status=status.HTTP_201_CREATED)
    


class LoginUserView(APIView):
    authentication_classes = []
    permission_classes = [AllowAny]

    def post(self, request):

        print("In views")

        serializer = LoginUserSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.validated_data['token'], status=status.HTTP_200_OK)

    



class RegisterVendorView(APIView):
    authentication_classes = []
    permission_classes = [AllowAny]

    def post(self, request):
    
        serializer = RegisterVendorSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

        return Response(serializer.save(), status=status.HTTP_201_CREATED)
    


class LoginVendorView(APIView):
    authentication_classes = []
    permission_classes = [AllowAny]

    def post(self, request):

        serializer = LoginVendorSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.validated_data['token'], status=status.HTTP_200_OK)