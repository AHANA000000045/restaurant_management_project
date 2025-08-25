# restaurant_management/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/menu/', include('menu.urls')),       # menu API
    path('api/orders/', include('orders.urls')),   # orders API
    path('api/accounts/', include('account.urls')),# account API
]
