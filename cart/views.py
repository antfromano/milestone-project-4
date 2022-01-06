from django.shortcuts import render, redirect, reverse, HttpResponse

# Create your views here.


def view_cart(request):
    """ view that renders cart page """

    return render(request, 'cart/cart.html')


def add_to_cart(request, work_id):
    """ Add a quantity of the specified product to the cart """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if work_id in list(cart.keys()):
        cart[work_id] += quantity
    else:
        cart[work_id] = quantity

    request.session['cart'] = cart
    return redirect(redirect_url)


def adjust_cart(request, work_id):

    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[work_id] = quantity
    else:
        del cart[work_id]
        if not cart[work_id]:
            cart.pop(work_id)

        request.session['cart'] = cart
        return redirect(reverse('view_cart'))


def remove_from_cart(request, work_id):
    """Remove the item from the cart"""

    try:
        quantity = int(request.POST.get('quantity'))
        cart = request.session.get('cart', {})

        if quantity > 0:
            del cart[work_id]
            if not cart[work_id]:
                cart.pop(work_id)
        else:
            cart.pop(work_id)

        request.session['cart'] = cart
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)
