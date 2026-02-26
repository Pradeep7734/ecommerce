from rest_framework import serializers
from .models import ProductCategory, Products

class ProductCategorySerailizer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = "__all__"
    


class ProductSerializer(serializers.ModelSerializer):

    description = serializers.CharField(required=False)
    quantity = serializers.FloatField(required=False)

    class Meta:
        model = Products
        fields = ["name", "description", "quantity", "sale_price", "category", "subcategory"]


    def create(self, validated_data):
        request = self.context['request']
        product = Products.objects.create(
            vendor = request.user,
            **validated_data
        )

        return product
    