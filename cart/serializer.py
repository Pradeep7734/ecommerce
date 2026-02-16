from rest_framework import serializers
from products.models import Products
from user.models import User
from .models import Cart, CartItems

class CartSerializer(serializers.Serializer):

    product = serializers.IntegerField()
    is_added = serializers.BooleanField(required=False, default=True)

    def create(self, validated_data):
        try:
            product_obj = Products.objects.get(pk=int(validated_data['product']))
            user_obj = self.context["request"].user
            print(f"Got the users: {user_obj}")
            # searching existing cart for the user
            existing_cart, is_new_cart = Cart.objects.get_or_create(user=user_obj)
            print(f"Existing cart: {existing_cart}")

            existing_cart_item, is_new_cart_item = CartItems.objects.get_or_create(cart=existing_cart, product=product_obj)

            if is_new_cart_item:
                if not validated_data['is_added']:
                    raise serializers.ValidationError("Cart cannot be in negative")
                
                existing_cart_item = CartItems.objects.create(
                    cart = existing_cart,
                    product = product_obj,
                    price = product_obj.sale_price,
                    quantity = 1
                )
            else:
                current_quantity = existing_cart_item.quantity
                existing_cart_item.objects.update(
                    quantity = current_quantity + 1,
                )

            return existing_cart_item

        except Products.DoesNotExist:
            raise serializers.ValidationError("Product does not exist")
        except Exception as e:
            raise serializers.ValidationError(f"Error occurred: {e}")

        
        