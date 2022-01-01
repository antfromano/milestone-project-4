from django.shortcuts import render
from .models import Work

# Create your views here.

def all_works(request):
    """ view to show all works, including sorting and search queries """

    works = Work.objects.all()

    context = {
        'works': works,
    }

    return render(request, 'works/works.html', context)
