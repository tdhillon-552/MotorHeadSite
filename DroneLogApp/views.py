from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test


def drone_user_test(user):
    return user.groups.filter(name__in=['dronelog_users'])


@user_passes_test(drone_user_test)
def home(request):
    return render(request, 'DroneLogApp/home.html')
