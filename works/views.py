from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Work, Content


# Create your views here.

def all_works(request):
    """ A view to show all works, including sorting and search queries """

    works = Work.objects.all()
    query = None
    contents = None
    sort = None
    direction = None

    if request.GET:

        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
                
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            works = works.order_by(sortkey)

        if 'content' in request.GET:
            contents = request.GET['content'].split(',')
            works = works.filter(content__name__in=contents)
            contents = Content.objects.filter(name__in=contents)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "you didn't enter search criteria")
                return redirect(reverse('works'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            works = works.filter(queries)

    context = {
        'works': works,
        'search_term': query,
        'current_contents': contents,
    }

    return render(request, 'works/works.html', context)


def work_item(request, work_id):
    """ A view to show individual work details """

    work = get_object_or_404(Work, pk=work_id)

    context = {
        'work': work,
    }

    return render(request, 'works/work_item.html', context)
