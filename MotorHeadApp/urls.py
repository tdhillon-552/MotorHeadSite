from django.urls import path
from . import views
from .views import DetailStats, EditStats

urlpatterns = [
    path('', views.home, name='home'),
    path('enterstats', views.EnterStats.as_view(), name='enterstats'),
    path('liststats', views.ListStats.as_view(), name='liststats'),
    path('detail/<int:pk>', DetailStats.as_view(), name='detailstats'),
    path('edit/<int:pk>', EditStats.as_view(), name='editstats')
]
