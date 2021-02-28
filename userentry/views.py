from django.views.generic import TemplateView

from home.models import PersoonsGegevens
from home.models import Doelstellingen
from home.models import Scorekaart
from django.shortcuts import get_object_or_404, render
from django.views import generic

from django.db.models import Sum


class IndexView(generic.ListView):
    template_name = 'userentry/index.html'
    context_object_name = 'latest_score_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return PersoonsGegevens.objects.order_by('-emailadres')[:5]


class PersoonsgegevensView(generic.DetailView):
    model = PersoonsGegevens
    template_name = 'userentry/persoonsgegevens.html'
    context_object_name = 'persoonsgegevens'

    def get_context_data(self, **kwargs):
        context = super(PersoonsgegevensView, self).get_context_data(**kwargs)
        context['doelstellingen'] = Doelstellingen.objects.values_list('persoonsgegevens_id', flat=True)
        return context


class DoelstellingenView(generic.DetailView):
    model = Doelstellingen
    template_name = 'userentry/doelstellingen.html'
    context_object_name = 'doelstellingen_list'

    def get_context_data(self, **kwargs):
        context = super(DoelstellingenView, self).get_context_data(**kwargs)
        PK = Doelstellingen.objects.get(pk=self.kwargs.get('pk'))
        context['doelstellingen'] = Doelstellingen.objects.filter(persoonsgegevens_id=PK.id)
        return context


class ScorekaartView(generic.DetailView):
    model = Scorekaart
    template_name = 'userentry/scorekaart.html'

    def get_context_data(self, **kwargs):
        context = super(ScorekaartView, self).get_context_data(**kwargs)
        context['scorekaart'] = Scorekaart.objects.aggregate(Sum('punten')).annotate(de)
        return context


def index(request):
    latest_score_list = PersoonsGegevens.objects.order_by('-emailadres')[:5]
    context = {'latest_score_list': latest_score_list}
#   context = {'Gebruikers': latest_score_list}
    return render(request, 'userentry/index.html', context)


def persoonsgegevens(request, persoonsgegevens_id):
    persoon = get_object_or_404(PersoonsGegevens, pk=persoonsgegevens_id)
    return render(request, 'userentry/detail.html', {'data': persoonsgegevens_id})


def doelstellingen(request, doelstellingen_id):
    doelstellingen_list = Doelstellingen.objects.all()
    context = {'doelstellingen_list': doelstellingen_list}
    return render(request, 'userentry/doelstellingen.html', context)