from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render

# Create your views here.
from django.views.generic import CreateView, ListView, DetailView, UpdateView

from .models import Stats
from .forms import StatsForm


def motorhead_user_test(user):
    return user.groups.filter(name__in=['motorhead_users'])


@user_passes_test(motorhead_user_test)
def home(request):
    return render(request, 'home.html')


class EnterStats(CreateView):
    model = Stats
    form_class = StatsForm
    template_name = 'enterstats.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(EnterStats, self).form_valid(form)


class ListStats(ListView):
    paginate_by = 5
    model = Stats
    template_name = 'liststats.html'
    ordering = ['-date']

    def get_queryset(self):
        return Stats.objects.filter(user=self.request.user)


class DetailStats(DetailView):
    model = Stats
    template_name = 'detailstats.html'


class EditStats(UpdateView):
    model = Stats
    form_class = StatsForm
    template_name = 'editstats.html'


