

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from orders.models import Order

class UpdateOrderStatus(APIView):
    allowed_transitions = {
        'Pending': ['Preparing'],
        'Preparing': ['Ready'],
        'Ready': ['Served'],
        'Served': []
    }

    def patch(self, request, pk):
        try:
            order = Order.objects.get(pk=pk)
        except Order.DoesNotExist:
            return Response({"error": "Order not found"}, status=status.HTTP_404_NOT_FOUND)

        new_status = request.data.get('status')
        if new_status in self.allowed_transitions[order.status]:
            order.status = new_status
            order.save()
            return Response({
                "id": order.id,
                "customer_name": order.customer_name,
                "status": order.status
            })
        return Response({"error": "Invalid status transition"}, status=status.HTTP_400_BAD_REQUEST)
