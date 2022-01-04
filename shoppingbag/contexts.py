from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from works.models import Work

def shoppingbag_sum(request):

    shoppingbag_items = []
    total = 0
    work_count = 0
    shoppingbag = request.session.get('shoppingbag', {})

    for work_id, quantity in shoppingbag.items():
        work = get_object_or_404(Work, pk=work_id)
        total += quantity * work.price
        work_count += quantity
        shoppingbag_items.append({
            'work_id': work_id,
            'quantity': quantity,
            'work': work,
        })
    
    delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)

    grand_total = delivery + total
    
    context = {
        'shoppingbag_items': shoppingbag_items,
        'total': total,
        'work_count': work_count,
        'delivery': delivery,
        'grand_total': grand_total,
    }

    return context
