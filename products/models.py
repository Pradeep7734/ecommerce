from django.db import models
from common.models import Common
from user.models import User

# Create your models here.
class ProductCategory(Common):

    name = models.CharField(max_length=50)
    parent = models.ForeignKey("self", on_delete=models.CASCADE, null=True,
                               blank=True, related_name="subcategories")
    
    def __str__(self):
        return self.name
    



class Products(Common):

    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    sale_price = models.FloatField()
    quantity = models.FloatField(default=1.0)
    vendor = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(ProductCategory, on_delete=models.SET_NULL, null=True, related_name="products")
    subcategory = models.ForeignKey(ProductCategory, on_delete=models.SET_NULL, null=True, related_name="sub_products")
