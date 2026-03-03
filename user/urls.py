from django.contrib import admin
from django.urls import path, include
from .views import RegisterUserView, LoginUserView


urlpatterns = [
    path('user/',RegisterUserView.as_view()),
    path('user-login/',LoginUserView.as_view()),
]
