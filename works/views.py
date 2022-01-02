from django.shortcuts import render, get_object_or_404
from .models import Work

# Create your views here.

def all_works(request):
    """ A view to show all works, including sorting and search queries """

    works = Work.objects.all()

    context = {
        'works': works,
    }

    return render(request, 'works/works.html', context)


def work_item(request, work_id):
    """ A view to show individual work details """

    work = get_object_or_404(Work, pk=work_id)

    context = {
        'work': work,
    }

    return render(request, 'works/work_item.html', context)
