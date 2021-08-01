from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
import DroneLogApp.urls
import MotorHeadApp.urls


@login_required
def home(request):
    return render(request, 'authhome.html')
