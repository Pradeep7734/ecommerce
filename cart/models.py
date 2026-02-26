from django.db import models
from user.models import User
from products.models import Products
from common.models import Common

# Create your models here.
class Cart(Common):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_amount = models.FloatField(default=0.0)
    total_product = models.FloatField(default=0)



class CartItems(models.Model):

    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    price = models.FloatField()
    quantity = models.FloatField()
