from django.db import models
import jwt
from datetime import datetime, timedelta, timezone

class Common(models.Model):

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True



class JWTHandler():

    SECRET = "8WQ5SAX2C1VB548GH7RE4W6S5XCV4871GFT/TF143EERTYHG+E486DF513B21Gew97864dsf513bgh+6fd2v"
    ALGORITHM = "HS256"

    def encode_jwt(claims):

        payload = {
            **claims,
            "iat": datetime.now(timezone.utc),
            "exp": datetime.now(timezone.utc) + timedelta(minutes=25),
        }

        return jwt.encode(
            payload=payload,
            key=JWTHandler.SECRET,
            algorithm=JWTHandler.ALGORITHM
        )
    
    def decode_jwt(encoded_jwt):

        return jwt.decode(
            jwt=encoded_jwt,
            key=JWTHandler.SECRET,
            algorithms=[JWTHandler.ALGORITHM]
        )
