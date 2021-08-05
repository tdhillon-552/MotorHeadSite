from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from .forms import MissionForm
from .models import MissionTable
from django.views.generic import CreateView, ListView, DetailView, UpdateView


def drone_user_test(user):
    return user.groups.filter(name__in=['dronelog_users'])


@user_passes_test(drone_user_test)
def home(request):
    return render(request, 'DroneLogApp/home.html')


class EnterDeployment(CreateView):
    model = MissionTable
    form_class = MissionForm
    template_name = 'DroneLogApp/enterdeployment.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(EnterDeployment, self).form_valid(form)
