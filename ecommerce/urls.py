from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('user.urls')),
    path('api/v1/', include('products.urls')),
    path('api/v1/', include('cart.urls')),
    # path('api/v1/', include('customer.urls')),
]
