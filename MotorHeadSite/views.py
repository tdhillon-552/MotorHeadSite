
from django.shortcuts import render
from django.shortcuts import redirect

import DroneLogApp.urls
import MotorHeadApp

def home(request):
    return render(request, 'authhome.html')


def login_success(request):
    """
    Redirects users based on whether they are in the admins group
    """
    if request.user.groups.filter(name="dronelog_users").exists():
        return redirect(DroneLogApp.urls.home)
    elif request.user.groups.filter(name="motorhead_users").exists():
        return redirect(MotorHeadApp.urls.home)
