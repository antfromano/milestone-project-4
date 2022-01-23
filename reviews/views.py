from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from works.models import Work
from .models import Review
from .forms import ReviewForm


@login_required
def review_work(request, work_id):
    """ review a work in the store """
    if not request.user.is_authenticated:
        messages.error(request, 'sorry, only registered users can do that.')
        return redirect(reverse('home'))

    work = get_object_or_404(Work, pk=work_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES, instance=work)
        if form.is_valid():
            form.save()
            messages.success(request, 'successfully reviewed work!')
            return redirect(reverse('work_item', args=[work.id]))
        else:
            messages.error(request, 'failed to review work. please ensure the form is valid.')
    else:
        form = ReviewForm(instance=work)
        messages.info(request, f'you are reviewing {work.name}')

    template = 'reviews/review_work.html'
    context = {
        'form': form,
        'work': work,
    }

    return render(request, template, context)
