from rest_framework import serializers
from .models import User, Profile
from cart.models import Cart
from django.db import transaction
from django.contrib.auth.hashers import make_password, check_password
from common.models import JWTHandler
from django.db.models import Q
import logging

logger = logging.getLogger(__name__)

class RegisterUserSerializer(serializers.Serializer):
    
    email = serializers.EmailField()
    phone_number = serializers.CharField(max_length=18)
    password = serializers.CharField(write_only=True)
    profile_type = serializers.CharField()

    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)

    def create(self, validated_data):
        logger.info(f"RegisterUserSerializer called")
        logger.debug(f"Got validated data: {validated_data}")
        with transaction.atomic():
            user = User.objects.create(
                email = validated_data['email'],
                phone_number = validated_data['phone_number'],
                password = make_password(validated_data['password']),
                profile_type = validated_data['profile_type']
            )

            Profile.objects.create(
                first_name = validated_data['first_name'],
                last_name = validated_data['last_name'],
                user_id = user,  
            )

            Cart.objects.create(
                user = user,
                total_amount = 0.0,
                total_product = 0
            )


            return {
                "token": JWTHandler.encode_jwt
                (
                    {
                    "id": user.id
                    }
                )
            }

    

class LoginUserSerializer(serializers.Serializer):

    login = serializers.CharField(max_length=250)
    password = serializers.CharField(write_only=True, max_length = 250)
    profile_type = serializers.CharField(required=False)

    def validate(self, validated_data):

        logger.info(f"LoginUserSerializer called")
        logger.debug(f"Got validated data: {validated_data}")

        login =  validated_data['login']
        password = validated_data['password']
        profile_type = validated_data.get("profile_type")

        query = Q(email=login) | Q(phone_number=login)

        if profile_type:
            logger.info(f"Going with profile filter")
            user = User.objects.filter(query, profile_type=profile_type).first()
        else:
            logger.info(f"Going without filter")
            user = User.objects.filter(query).first()

        logger.info(f"User fetched successfully from db: {user}")

        if not user:
            logger.warning(f"User not found!.")
            raise serializers.ValidationError("User Not Found!.")
        

        if user and check_password(password, user.password):
            logger.info(f"Generating token for the user.")
            validated_data['token'] = {
                "token": JWTHandler.encode_jwt
                (
                    {
                    "id": user.id,
                    "role": user.profile_type
                    }
                )
            }
            logger.info(f"Token generated successfully.")
            return validated_data
        
        raise serializers.ValidationError("Invalid Credentials.")
