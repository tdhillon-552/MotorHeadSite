
from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('motorhead/', include('MotorHeadApp.urls'), name='motorheadpush'),
    path('dronelog/', include('DroneLogApp.urls'), name='dronelogpush'),
    path('', views.home, name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
]
