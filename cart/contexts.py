from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from works.models import Work

def cart_sum(request):

    cart_items = []
    total = 0
    work_count = 0
    cart = request.session.get('cart', {})

    for work_id, quantity in cart.items():
        work = get_object_or_404(Work, pk=work_id)
        total += quantity * work.price
        work_count += quantity
        cart_items.append({
            'work_id': work_id,
            'quantity': quantity,
            'work': work,
        })
    
    delivery_cost = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)

    grand_total = delivery_cost + total
    
    context = {
        'cart_items': cart_items,
        'total': total,
        'work_count': work_count,
        'delivery_cost': delivery_cost,
        'grand_total': grand_total,
    }

    return context
