from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Work, Content, Review
from .forms import WorkForm, ReviewForm
from decimal import Decimal

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
    all_reviews = Review.objects.filter(work=work)
    try:
        average_rating = round(sum([i.user_rating for i in all_reviews])/all_reviews.count(), 2)
    except ZeroDivisionError:
        average_rating = 0
      
    context = {
        'work': work,
        'average_rating': average_rating,
        'all_reviews': all_reviews,
    }

    return render(request, 'works/work_item.html', context)


@login_required
def add_work(request):
    """ Add a work to the store """
    if not request.user.is_superuser:
        messages.error(request, 'sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = WorkForm(request.POST, request.FILES)
        if form.is_valid():
            work = form.save()
            messages.success(request, 'successfully added work!')
            return redirect(reverse('work_item', args=[work.id]))
        else:
            messages.error(request, 'failed to add work. please ensure the form is valid.')
    else:
        form = WorkForm()

    template = 'works/add_work.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_work(request, work_id):
    """ Edit a work in the store """
    if not request.user.is_superuser:
        messages.error(request, 'sorry, only store owners can do that.')
        return redirect(reverse('home'))
    work = get_object_or_404(Work, pk=work_id)
    if request.method == 'POST':
        form = WorkForm(request.POST, request.FILES, instance=work)
        if form.is_valid():
            form.save()
            messages.success(request, 'successfully updated work!')
            return redirect(reverse('work_item', args=[work.id]))
        else:
            messages.error(request, 'failed to update work. please ensure the form is valid.')
    else:
        form = WorkForm(instance=work)
        messages.info(request, f'you are editing {work.name}')
    template = 'works/edit_work.html'
    context = {
        'form': form,
        'work': work,
    }
    return render(request, template, context)


@login_required
def delete_work(request):
    """ Delete a work from the store """
    if not request.user.is_superuser:
        messages.error(request, 'sorry, only store owners can do that.')
        return redirect(reverse('home'))

    work = get_object_or_404(Work, pk=work_id)
    work.delete()
    messages.success(request, 'work deleted!')
    return redirect(reverse('works'))

@login_required
def review_work(request, work_id):
    """Review a work in the store"""
    
    work = get_object_or_404(Work, pk=work_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            
            f = ReviewForm(request.POST)
            new_review = f.save(commit=False)
            new_review.work = work
            new_review.save()

            messages.success(request, 'successfully reviewed work!')
            return redirect(reverse('work_item', args=[work.id]))
            
        else:
            messages.error(request, 'failed to review work. please ensure the form is valid.')
    else:
        form = ReviewForm()

    form = ReviewForm(instance=work)
    messages.info(request, f'you are reviewing {work.name}')

    template = 'works/review_work.html'
    context = {
        'form': form,
        'work': work,
    }

    return render(request, template, context)
