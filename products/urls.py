from django.urls import path, include
from .views import ProductCategoryViewSet, ProductsView
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'products/category', ProductCategoryViewSet)
router.register(r'products/product', ProductsView)


urlpatterns = [
    path("", include(router.urls)),
    # path("products/", ProductsView.as_view()),
    # path("products/<int:pk>/", ProductsView.as_view())
]
