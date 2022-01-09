from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages

from works.models import Work


def view_cart(request):
    """ view to render cart page """

    return render(request, 'cart/cart.html')


def add_to_cart(request, work_id):
    """ add specified work to cart """

    work = get_object_or_404(Work, pk=work_id)
    quantity = 1
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    cart[work_id] = quantity
    messages.success(request, f'added {work.name} to your cart')

    request.session['cart'] = cart
    return redirect(redirect_url)


def remove_from_cart(request, work_id):
    """ remove work from cart"""

    try:
        work = get_object_or_404(Work, pk=work_id)
        cart = request.session.get('cart', {})

        cart.pop(work_id)
        messages.success(request, f'removed {work.name} from your cart')

        request.session['cart'] = cart
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'error removing work')
        return HttpResponse(status=500)
