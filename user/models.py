from django.db import models
from common.models import Common

# Create your models here.
class User(Common):

    email = models.EmailField(max_length=255, unique=True)
    phone_number = models.CharField(max_length=18, unique=True)
    password = models.CharField(max_length=250)
    profile_type = models.CharField(choices=(
        ('C', 'Customer'),
        ('V', 'Vendor'),
    ))
    
    class Meta:
        unique_together = ['email', 'phone_number']
        


class Profile(Common):

    user_id = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    