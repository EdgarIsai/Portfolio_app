from django.shortcuts import render, get_object_or_404

from .models import Hostel
from .forms import NameForm


def hostel_index(request):
    search_term = ""
    hostels = Hostel.objects.all().order_by('-updated')

    if 'search' in request.GET:
        search_term = request.GET['search']
        hostels = hostels.filter(name__icontains=search_term)

    context = {
        'hostels': hostels,
        'search_term': search_term,
    }

    return render(request, 'hostel_index.html', context)


def get_name(request):
    form = NameForm()
    return render(request, 'hostel_detail.html', {'form': form})


def post_detail(request, year, month, day, post):
    search_term = ""
    hostels = Hostel.objects.all().order_by('-updated')

    if 'search' in request.GET:
        search_term = request.GET['search']
        hostels = hostels.filter(name__icontains=search_term)

        context = {
            'hostels': hostels,
            'search_term': search_term,
        }

        return render(request, 'hostel_detail.html', context)

    post = get_object_or_404(Hostel, slug=post,
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)

    return render(request, 'hostel_detail.html', {'hostel': post})


def help_form(request):
    search_term = ""
    hostels = Hostel.objects.all().order_by('-updated')

    if 'search' in request.GET:
        search_term = request.GET['search']
        hostels = hostels.filter(name__icontains=search_term)

        context = {
            'hostels': hostels,
            'search_term': search_term,
        }

        return render(request, 'hostel_detail.html', context)
    return render(request, 'help.html')
