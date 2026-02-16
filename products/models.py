from django.db import models
from common.models import Common
from user.models import User

# Create your models here.
class ProductCategory(Common):

    name = models.CharField(max_length=50)
    vendor = models.ForeignKey(User, on_delete=models.CASCADE)



class Products(Common):

    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    sale_price = models.FloatField()
    purchase_price = models.FloatField()
    quantity = models.FloatField(default=1.0)
    vendor = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
