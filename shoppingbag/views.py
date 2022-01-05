from django.shortcuts import render, redirect, reverse, HttpResponse

# Create your views here.


def view_shoppingbag(request):
    """ view that renders shoppingbag page """

    return render(request, 'shoppingbag/shoppingbag.html')


def add_to_shoppingbag(request, work_id):
    """ Add a quantity of the specified product to the shoppingbag """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    shoppingbag = request.session.get('shoppingbag', {})

    if work_id in list(shoppingbag.keys()):
        shoppingbag[work_id] += quantity
    else:
        shoppingbag[work_id] = quantity

    request.session['shoppingbag'] = shoppingbag
    return redirect(redirect_url)


def adjust_shoppingbag(request, work_id):

    quantity = int(request.POST.get('quantity'))
    shoppingbag = request.session.get('shoppingbag', {})

    if quantity > 0:
        shoppingbag[work_id] = quantity
    else:
        del shoppingbag[work_id]
        if not shoppingbag[work_id]:
            shoppingbag.pop(work_id)

        request.session['shoppingbag'] = shoppingbag
        return redirect(reverse('view_shoppingbag'))


def remove_from_shoppingbag(request, work_id):
    """Remove the item from the shoppingbag"""

    try:
        quantity = int(request.POST.get('quantity'))
        shoppingbag = request.session.get('shoppingbag', {})

        if quantity > 0:
            del shoppingbag[work_id]
            if not shoppingbag[work_id]:
                shoppingbag.pop(work_id)
        else:
            shoppingbag.pop(work_id)

        request.session['shoppingbag'] = shoppingbag
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)
