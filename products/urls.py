from django.urls import path, include
from .views import ProductCategoryView, ProductsView

urlpatterns = [
    path("products/category/", ProductCategoryView.as_view()),
    path("products/category/<int:pk>/", ProductCategoryView.as_view()),
    path("products/", ProductsView.as_view()),
    path("products/<int:pk>/", ProductsView.as_view())
]
