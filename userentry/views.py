from home.models import PersoonsGegevens
from home.models import Activiteiten
from home.models import Doelstellingen
from home.models import Scorekaart
from django.shortcuts import get_object_or_404, render
from django.views import generic


class IndexView(generic.ListView):
    template_name = 'userentry/index.html'
    context_object_name = 'latest_score_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return PersoonsGegevens.objects.order_by('-emailadres')[:5]


class DetailView(generic.DetailView):
    model = PersoonsGegevens
    template_name = 'userentry/persoonsgegevens.html'
    context_object_name = 'latest_score_list'


class PersoonsgegevensView(generic.DetailView):
    model = PersoonsGegevens
    template_name = 'userentry/persoonsgegevens.html'
    context_object_name = 'latest_score_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return PersoonsGegevens.objects.order_by('-emailadres')[:5]


class DoelstellingenView(generic.DetailView):
    model = Doelstellingen
    template_name = 'userentry/doelstellingen.html'
    context_object_name = 'latest_score_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Doelstellingen.objects.order_by('activiteiten_id')


class ScorekaartView(generic.DetailView):
    model = Scorekaart
    template_name = 'userentry/scorekaart.html'


def index(request):
    latest_score_list = PersoonsGegevens.objects.order_by('-emailadres')[:5]
    context = {'latest_score_list': latest_score_list}
#   context = {'Gebruikers': latest_score_list}
    return render(request, 'userentry/index.html', context)


def persoonsgegevens(request, persoonsgegevens_id):
    persoon = get_object_or_404(PersoonsGegevens, pk=persoonsgegevens_id)
    return render(request, 'userentry/detail.html', {'data': persoonsgegevens_id})


def doelstellingen(request, doelstellingen_id):
    persoon = get_object_or_404(PersoonsGegevens, pk=doelstellingen_id)
    return render(request, 'userentry/doelstellingen.html', {'data': doelstellingen_id})