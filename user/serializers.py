from rest_framework import serializers
from .models import User, Profile
from cart.models import Cart
from django.db import transaction
from django.contrib.auth.hashers import make_password, check_password
from common.models import JWTHandler
from django.db.models import Q
import logging
from utility_folder.user_type import USER_PROFILE_TYPE

logger = logging.getLogger(__name__)


class RegisterUserSerializer(serializers.Serializer):
    
    login = serializers.CharField(max_length=255)
    profile_type = serializers.ChoiceField(choices=USER_PROFILE_TYPE, default=USER_PROFILE_TYPE[0][0])

    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)

    def create(self, validated_data):
        logger.info(f"RegisterUserSerializer called")
        logger.debug(f"Got validated data: {validated_data}")

        User.objects.create(

        )


class LoginUserSerializer(serializers.Serializer):

    login = serializers.CharField(max_length=250)
    profile_type = serializers.ChoiceField(choices=USER_PROFILE_TYPE, choicrequired=False)

    def validate(self, validated_data):

        logger.info(f"LoginUserSerializer called")
        logger.debug(f"Got validated data: {validated_data}")

        login = validated_data['login']
        profile_type = validated_data.get('profile_type')


        if not profile_type:
            logger.debug("Finding user without profile type")
            user = User.objects.filter(Q(login=login)).first()
        else:
            logger.debug("Finding user with profile type")
            user = User.objects.filter(Q(login=login) , Q(profile_type=profile_type)).first()

        logger.info(f"User fetched successfully from db: {user}")

        if not user:
            logger.warning(f"User not found!.")
            raise serializers.ValidationError("Invalid Credentials!.")
        

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
