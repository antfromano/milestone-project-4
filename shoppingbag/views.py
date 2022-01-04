from django.shortcuts import render, redirect

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
    print(request.session['shoppingbag'])
    return redirect(redirect_url)
