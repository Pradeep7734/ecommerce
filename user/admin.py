from django.contrib import admin
from .models import User, Profile

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["id", "email", "phone_number", "password", "profile_type", "is_active", "created_at", "updated_at"]
    list_filter = ["is_active", "created_at", "updated_at"]
    search_fields = ["email", "phone_number"]


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ["id", "first_name", "last_name", "user_id", "is_active", "created_at", "updated_at"]
    list_filter = ["is_active", "created_at", "updated_at"]
    search_fields = ["first_name", "last_name", "user_id"]