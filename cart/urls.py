from django.urls import path, include
from .views import CartItemsView

urlpatterns = [
    path("cart/", CartItemsView.as_view()),
]
