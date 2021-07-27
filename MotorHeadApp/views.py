from django.shortcuts import render

# Create your views here.
from django.views.generic import CreateView

from .models import Stats
from .forms import StatsForm


def home(request):
    return render(request, 'home.html')


class EnterStats(CreateView):
    model = Stats
    form_class = StatsForm
    template_name = 'enterstats.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(EnterStats, self).form_valid(form)
