from django.shortcuts import render

# Create your views here.

def view_shoppingbag(request):
    """ view that renders shoppingbag page """

    return render(request, 'shoppingbag/shoppingbag.html')
    