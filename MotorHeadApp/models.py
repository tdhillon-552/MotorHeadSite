
from django.utils.timezone import now
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.urls import reverse


class Stats(models.Model):
    date = models.DateField(default=now(), blank=False)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    court = models.FloatField(default=0)
    personal = models.FloatField(default=0)
    training = models.FloatField(default=0)
    equipment = models.FloatField(default=0)
    meetings = models.FloatField(default=0)
    accident = models.FloatField(default=0)
    crime = models.FloatField(default=0)
    patrol_coverage = models.FloatField(default=0)
    call_out = models.FloatField(default=0)
    other = models.FloatField(default=0)
    enforcement_stops = models.IntegerField(default=0)
    citations = models.IntegerField(default=0)
    mechanicals = models.IntegerField(default=0)
    OTS_Cites = models.IntegerField(default=0)
    complaint_areas = models.IntegerField(default=0)
    accident_reports = models.IntegerField(default=0)
    accident_sups = models.IntegerField(default=0)
    arrests = models.IntegerField(default=0)
    NAT = models.IntegerField(default=0)

    def get_absolute_url(self):
        return reverse('home')
