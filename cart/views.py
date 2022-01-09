from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages

from works.models import Work

# Create your views here.


def view_cart(request):
    """ view that renders cart page """

    return render(request, 'cart/cart.html')


def add_to_cart(request, work_id):
    """ Add a quantity of the specified work to the cart """

    work = get_object_or_404(Work, pk=work_id)
    quantity = 1
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if work_id in list(cart.keys()):
        cart[work_id] += quantity
        messages.success(request, f'updated {work.name} quantity to {cart[work_id]}')

    else:
        cart[work_id] = quantity
        messages.success(request, f'added {work.name} to your cart')

    request.session['cart'] = cart
    return redirect(redirect_url)


def adjust_cart(request, work_id):

    work = get_object_or_404(Work, pk=work_id)
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity:
        if quantity > 0:
            cart[work_id] = quantity
            messages.success(request, f'updated {work.name} quantity to {cart[work_id]}')
        else:
            del cart[work_id]
            if not cart[work_id]:
                cart.pop(work_id)
            messages.success(request, f'removed {work.name} from your cart')
    else:
        if quantity > 0:
            cart[work_id] = quantity
            messages.success(request, f'updated {work.name} quantity to {cart[work_id]}')
        else: 
            cart.pop(work_id)
            messages.success(request, f'removed {work.name} from your cart')

        request.session['cart'] = cart
        return redirect(reverse('view_cart'))


def remove_from_cart(request, work_id):
    """Remove the item from the cart"""

    try:
        work = get_object_or_404(Work, pk=work_id)
        quantity = int(request.POST.get('quantity'))
        cart = request.session.get('cart', {})

        if quantity > 0:
            del cart[work_id]
            if not cart[work_id]:
                cart.pop(work_id)
            messages.success(request, f'removed {work.name} from your cart')
        else:
            cart.pop(work_id)
            messages.success(request, f'removed {work.name} from your cart')

        request.session['cart'] = cart
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'error removing work')
        return HttpResponse(status=500)
