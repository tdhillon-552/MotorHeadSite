from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView
from .models import Stats
from .forms import StatsForm, UpdateStatsForm, SearchByMotor, SearchTotalsForm


def motorhead_user_test(user):
    return user.groups.filter(name__in=['motorhead_users'])


@user_passes_test(motorhead_user_test)
def home(request):
    return render(request, 'MotorHeadApp/home.html')


class EnterStats(CreateView):
    model = Stats
    form_class = StatsForm
    template_name = 'MotorHeadApp/enterstats.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(EnterStats, self).form_valid(form)

    def get_success_url(self):
        if 'add_another' in self.request.POST:
            url = reverse_lazy('enterstats')
        else:
            url = reverse('detailstats', args=(self.object.id,))
        return url


class ListStats(ListView):
    paginate_by = 5
    model = Stats
    template_name = 'MotorHeadApp/liststats.html'
    ordering = ['-date']

    def get_queryset(self):
        return Stats.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super(ListStats, self).get_context_data(**kwargs)
        context['calendarstats'] = Stats.objects.filter(user=self.request.user)
        return context


class DetailStats(DetailView):
    model = Stats
    template_name = 'MotorHeadApp/detailstats.html'


class EditStats(UpdateView):
    model = Stats
    form_class = UpdateStatsForm
    template_name = 'MotorHeadApp/editstats.html'


def searchbymotor(request):

    if request.POST:
        form_data = SearchByMotor(request.POST)
        if form_data.is_valid():
            start_date = form_data.cleaned_data['start_date']
            end_date = form_data.cleaned_data['end_date']
            searched_motor = form_data.cleaned_data['motor']

            request.session['pass_start_date_stats'] = start_date
            request.session['pass_end_date_stats'] = end_date
            request.session['pass_searched_motor_stats'] = request.POST.get('motor')

            search_query = Stats.objects.filter(date__range=[start_date, end_date], user=searched_motor)
            search_results = {
                'court': sum(total.court for total in search_query),
                'personal': sum(total.personal for total in search_query),
                'training': sum(total.training for total in search_query),
                'equipment': sum(total.equipment for total in search_query),
                'meetings': sum(total.meetings for total in search_query),
                'accident': sum(total.accident for total in search_query),
                'crime': sum(total.crime for total in search_query),
                'patrol_coverage': sum(total.patrol_coverage for total in search_query),
                'call_out': sum(total.call_out for total in search_query),
                'other': sum(total.other for total in search_query),
                'enforcement_stops': sum(total.enforcement_stops for total in search_query),
                'citations': sum(total.citations for total in search_query),
                'mechanicals': sum(total.mechanicals for total in search_query),
                'OTS_Cites': sum(total.OTS_Cites for total in search_query),
                'complaint_areas': sum(total.complaint_areas for total in search_query),
                'accident_reports': sum(total.accident_reports for total in search_query),
                'accident_sups': sum(total.accident_sups for total in search_query),
                'arrests': sum(total.arrests for total in search_query),
                'NAT': sum(total.NAT for total in search_query),

            }
    else:
        form_data = SearchByMotor()
        search_results = None

    content = {
        'form_data': form_data,
        'search_results': search_results,
    }

    return render(request, 'MotorHeadApp/searchbymotor.html', content)


def searchtotals(request):

    if request.POST:
        form_data = SearchTotalsForm(request.POST)
        if form_data.is_valid():
            start_date = form_data.cleaned_data['start_date']
            end_date = form_data.cleaned_data['end_date']

            request.session['pass_start_date_totals'] = start_date
            request.session['pass_end_date_totals'] = end_date
            request.session['pass_searched_motor_totals'] = request.POST.get('motor')

            search_query = Stats.objects.filter(date__range=[start_date, end_date])
            search_results = {
                'court': sum(total.court for total in search_query),
                'personal': sum(total.personal for total in search_query),
                'training': sum(total.training for total in search_query),
                'equipment': sum(total.equipment for total in search_query),
                'meetings': sum(total.meetings for total in search_query),
                'accident': sum(total.accident for total in search_query),
                'crime': sum(total.crime for total in search_query),
                'patrol_coverage': sum(total.patrol_coverage for total in search_query),
                'call_out': sum(total.call_out for total in search_query),
                'other': sum(total.other for total in search_query),
                'enforcement_stops': sum(total.enforcement_stops for total in search_query),
                'citations': sum(total.citations for total in search_query),
                'mechanicals': sum(total.mechanicals for total in search_query),
                'OTS_Cites': sum(total.OTS_Cites for total in search_query),
                'complaint_areas': sum(total.complaint_areas for total in search_query),
                'accident_reports': sum(total.accident_reports for total in search_query),
                'accident_sups': sum(total.accident_sups for total in search_query),
                'arrests': sum(total.arrests for total in search_query),
                'NAT': sum(total.NAT for total in search_query),

            }
    else:
        form_data = SearchByMotor()
        search_results = None

    content = {
        'form_data': form_data,
        'search_results': search_results,
    }

    return render(request, 'MotorHeadApp/searchtotals.html', content)


