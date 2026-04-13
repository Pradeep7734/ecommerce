from django.db import models
from common.models import Common
from utility_folder.user_type import USER_PROFILE_TYPE

# Create your models here.
class User(Common):

    login = models.CharField(max_length=255, unique=True)
    profile_type = models.CharField(choices=USER_PROFILE_TYPE)
        


class Profile(Common):

    user_id = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    