from rest_framework import serializers
from .models import User, Profile
from cart.models import Cart
from django.db import transaction
from django.contrib.auth.hashers import make_password, check_password
from common.models import JWTHandler

class RegisterUserSerializer(serializers.Serializer):
    
    email = serializers.EmailField()
    phone_number = serializers.CharField(max_length=50)
    password = serializers.CharField(write_only=True)

    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)

    def create(self, validated_data):
        with transaction.atomic():
            user = User.objects.create(
                email = validated_data['email'],
                phone_number = validated_data['phone_number'],
                password = make_password(validated_data['password']),
                profile_type = 'C'
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
    password = serializers.CharField(write_only=True, max_length = 50)

    def validate(self, validated_data):

        print("In serializer")

        login =  validated_data['login']
        password = validated_data['password']

        if '@' in login:
            user = User.objects.filter(email=login, profile_type='C').first()
        else:
            user = User.objects.filter(phone_number=login, profile_type='C').first()


        if user and check_password(password, user.password):

            validated_data['token'] = {
                "token": JWTHandler.encode_jwt
                (
                    {
                    "id": user.id
                    }
                )
            }
            return validated_data
        
        raise serializers.ValidationError("Invalid Credentials.")



class RegisterVendorSerializer(serializers.Serializer):
    
    email = serializers.EmailField()
    phone_number = serializers.CharField(max_length=50)
    password = serializers.CharField(write_only=True)

    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)

    def create(self, validated_data):
        with transaction.atomic():
            user = User.objects.create(
                email = validated_data['email'],
                phone_number = validated_data['phone_number'],
                password = make_password(validated_data['password']),
                profile_type = 'V'
            )

            Profile.objects.create(
                first_name = validated_data['first_name'],
                last_name = validated_data['last_name'],
                user_id = user,
                
            )

            return {
                "token": JWTHandler.encode_jwt
                (
                    {
                    "id": user.id
                    }
                )
            }


class LoginVendorSerializer(serializers.Serializer):

    login = serializers.CharField(max_length=250)
    password = serializers.CharField(write_only=True, max_length = 50)

    def validate(self, validated_data):

        login =  validated_data['login']
        password = validated_data['password']

        if '@' in login:
            user = User.objects.filter(email=login, profile_type='V').first()
        else:
            user = User.objects.filter(phone_number=login, profile_type='V').first()


        if user and check_password(password, user.password):
            validated_data['token'] = {
                "token": JWTHandler.encode_jwt
                (
                    {
                    "id": user.id
                    }
                )
            }
            return validated_data
        
        raise serializers.ValidationError("Invalid Credentials.")