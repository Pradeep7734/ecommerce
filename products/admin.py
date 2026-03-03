from django.contrib import admin
from .models import ProductCategory, Products

# Register your models here.

@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "parent", "is_active", "created_at")
    list_filter = ("is_active", "parent")
    search_fields = ("name",)


@admin.register(Products)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', "name", "description", "sale_price", "quantity", "vendor", "category", "subcategory"]
    search_fields = ["name"]
