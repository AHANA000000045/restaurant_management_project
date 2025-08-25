from .models import Menu
from .serializers import MenuSerializer
from rest_framework import generics

class MenuAPIView(generics.ListAPIView):
    queryset = Menu.objects.select_related('category').all()
    serializer_class = MenuSerializer






