from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from common.models import JWTHandler
from user.models import User

class JWTAuthentication(BaseAuthentication):

    def authenticate(self, request):
        print("In auth")
        auth = request.headers.get("Authorization")
        print(f"Auth: {auth}")

        if not auth:
            raise AuthenticationFailed("Authentication credentials were not provided.")

        try:
            print(f"I am in try")
            token = auth.split(" ")[1]
            payload = JWTHandler.decode_jwt(token)
            user = User.objects.get(id=payload["id"])
            print(f"Got the user: {user}")
            return (user, None)
        except IndexError:
            raise AuthenticationFailed("Invalid Authorization header format.")

        except User.DoesNotExist:
            raise AuthenticationFailed("User not found.")

        except Exception:
            raise AuthenticationFailed("Invalid or expired token.")