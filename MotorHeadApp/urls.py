from django.urls import path
from . import views
from .views import DetailStats, EditStats
from . import printviews

urlpatterns = [
    path('', views.home, name='home'),
    path('enterstats', views.EnterStats.as_view(), name='enterstats'),
    path('liststats', views.ListStats.as_view(), name='liststats'),
    path('detail/<int:pk>', DetailStats.as_view(), name='detailstats'),
    path('edit/<int:pk>', EditStats.as_view(), name='editstats'),
    path('searchmotor', views.searchbymotor, name='searchbymotor'),
    path('searchmotor/print', printviews.statsprint, name='statsprint'),
    path('searchtotals', views.searchtotals, name='searchtotals'),
    path('searchtotals/print', printviews.totalsprint, name='totalsprint'),
]
