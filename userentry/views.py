from django.shortcuts import render
from django.views import generic

from . models import PersoonsGegevens


class IndexView(generic.ListView):
    template_name = 'userentry/index.html'
    context_object_name = 'latest_score_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return PersoonsGegevens.objects.order_by('-emailadres')[:5]


def index(request):
    latest_score_list = PersoonsGegevens.objects.order_by('-emailadres')[:5]
    context = {'latest_score_list': latest_score_list}
#   context = {'Gebruikers': latest_score_list}
    return render(request, 'userentry/index.html', context)


def detail(request):
    latest_score_list = PersoonsGegevens.objects.order_by('-emailadres')[:5]
    context = {'latest_score_list': latest_score_list}
    #   context = {'Gebruikers': latest_score_list}
    return render(request, 'userentry/index.html', context)
