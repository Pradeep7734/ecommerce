import logging
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import RegisterUserSerializer, LoginUserSerializer
from rest_framework import status
from rest_framework.permissions import AllowAny

logger = logging.getLogger(__name__)

class RegisterUserView(APIView):
    authentication_classes = []
    permission_classes = [AllowAny]

    def post(self, request):

        logger.info("RegisterUserView called")
        logger.debug(f"Incoming data: {request.data}")
    
        serializer = RegisterUserSerializer(data=request.data)

        if not serializer.is_valid():
            logger.warning("User registration validation failed")
            logger.debug(f"Validation errors: {serializer.errors}")
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        user = serializer.save()
        logger.info(f"User registered successfully: {user}")

        return Response(user, status=status.HTTP_201_CREATED)
    


class LoginUserView(APIView):
    authentication_classes = []
    permission_classes = [AllowAny]

    def post(self, request):
        try:
            logger.info("LoginUserView called")
            logger.debug(f"Incoming data: {request.data}")

            serializer = LoginUserSerializer(data=request.data)

            if not serializer.is_valid():
                logger.warning("User login validation failed")
                logger.debug(f"Validation errors: {serializer.errors}")
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
            token = serializer.validated_data['token']
            logger.info(f"User login successfully: {token}")

            return Response(token, status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response({
                "error": str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)