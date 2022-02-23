from django.shortcuts import render

# create your views here.

def index(request):
    """ view to return index page """

    return render(request, 'home/index.html')
