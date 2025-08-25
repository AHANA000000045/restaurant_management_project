from celery import shared_task
from orders.models import Order
from datetime import date
from django.db.models import Count, Sum

@shared_task
def generate_sales_report():
    total_orders = Order.objects.count()
    total_sales = Order.objects.aggregate(total=Sum('total_price'))['total'] or 0
    top_item_qs = Order.objects.values('items__name').annotate(count=Count('items')).order_by('-count').first()
    top_item = top_item_qs['items__name'] if top_item_qs else None

    report = {
        "date": str(date.today()),
        "total_orders": total_orders,
        "total_sales": total_sales,
        "top_item": top_item
    }
    # You can save this in a SalesReport model if needed
    print(report)
    return report
