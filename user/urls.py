from django.contrib import admin
from django.urls import path, include
from .views import RegisterUserView, RegisterVendorView, LoginUserView, LoginVendorView


urlpatterns = [
    path('user/',RegisterUserView.as_view()),
    path('user-login/',LoginUserView.as_view()),
    path('vendor/',RegisterVendorView.as_view()),
    path('vendor-login/',LoginVendorView.as_view()),
]
