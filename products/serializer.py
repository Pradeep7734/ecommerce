from rest_framework import serializers
from .models import ProductCategory, Products

class ProductCategorySerailizer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = "__all__"
    


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Products
        fields = "__all__"
        read_only_fields = ["vendor"]
    