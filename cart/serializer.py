import logging
from rest_framework import serializers
from products.models import Products
from .models import CartItems, Cart
from django.db.models import F
from django.db import transaction

logger = logging.getLogger(__name__)

class CartItemsSerializer(serializers.Serializer):

    product_id = serializers.IntegerField()

    def create(self, validated_data):
        user_obj = self.context['request'].user
        logger.info(f"User: {user_obj}")

        logger.info("CartItemsSerializer create called")
        logger.debug(f"Got data : {validated_data}")

        product = Products.objects.filter(id=validated_data['product_id'], is_active=True).first()
        logger.info(f"Fetched product from db: {product}")

        if not product:
            raise serializers.ValidationError(f"Product not found.")

        with transaction.atomic():

            cart, _ = Cart.objects.get_or_create(user=user_obj)
            logger.info(f"Cart: {cart}")

            cart_item, cart_item_created = CartItems.objects.update_or_create(
                cart = cart,
                product = product,
                defaults={"quantity": 1}
            )

            if cart_item_created:
                Cart.objects.filter(id=cart.id).update(
                    total_product = F("total_product") + 1
                )

        return cart_item

