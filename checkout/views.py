from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings
from .forms import OrderForm
from cart.contexts import cart_sum 

import stripe

# Create your views here.


def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "There's nothing in your cart at the moment")
        return redirect(reverse('works'))
    
    current_cart = cart_sum(request)
    total = current_cart['grand_total']
    stripe_total = round(total * 100)
    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51KG3WcCUV5kYkVNmHvUYe4yGuVGphQxL2s1BFAz7hxQyfVsXpJN28L6DCoAADpDiWD4Q2BxTUcAmhYJ31MVQdoX500qY5PRYeU',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
