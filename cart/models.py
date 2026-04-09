from django.db import models
from user.models import User
from products.models import Products
from common.models import Common

# Create your models here.
class Cart(Common):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_product = models.DecimalField(max_digits=3, decimal_places=2)



class CartItems(models.Model):

    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['cart', 'product'],
                name = 'unique_cart_product'
            )
        ]
