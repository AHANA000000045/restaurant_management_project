from django.urls import path
from .views import UpdateOrderStatus

urlpatterns = [
    path('<int:pk>/update-status/', UpdateOrderStatus.as_view(), name='update-order-status'),
]
