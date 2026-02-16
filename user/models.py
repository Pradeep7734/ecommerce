from django.db import models
from common.models import Common

# Create your models here.
class User(Common):

    email = models.CharField(max_length=255, unique=True)
    phone_number = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=250)
    profile_type = models.CharField(max_length=50, choices=(
        ('C', 'Customer'),
        ('V', 'Vendor'),
    ))


class Profile(Common):

    user_id = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    