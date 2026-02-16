from rest_framework import serializers
from .models import ProductCategory, Products

class ProductCategorySerailizer(serializers.ModelSerializer):

    is_active = serializers.BooleanField(read_only=True)
    class Meta:
        model = ProductCategory
        fields = ["name", "is_active"]

    def create(self, validated_data):
        request = self.context['request']
        category = ProductCategory.objects.create(
            vendor = request.user,
            name = validated_data['name']
        )
        return category
    


class ProductSerializer(serializers.ModelSerializer):
    description = serializers.CharField(required=False)
    quantity = serializers.FloatField(required=False)
    class Meta:
        model = Products
        fields = ["name", "description", "sale_price", "purchase_price", "quantity", "category"]


    def create(self, validated_data):
        request = self.context['request']
        product = Products.objects.create(
            vendor = request.user,
            **validated_data
        )

        return product
    