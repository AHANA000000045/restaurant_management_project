from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from products.views import ProductViewSet
from orders.views import OrderViewSet

router = routers.DefaultRouter()
router.register('menu', ProductViewSet, basename='menu')
router.register('orders', OrderViewSet, basename='orders')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/accounts/', include('account.urls')),
]
