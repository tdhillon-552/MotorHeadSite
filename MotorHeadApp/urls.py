from django.urls import path
from . import views



urlpatterns = [
    path('', views.home, name='home'),
    path('enterstats', views.EnterStats.as_view(), name='enterstats'),
    ]
