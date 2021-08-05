from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.timezone import now


class DroneTable(models.Model):
    name = models.CharField(max_length=50, default="")
    make = models.CharField(max_length=50, default="")
    model = models.CharField(max_length=50, default="")
    serial = models.CharField(max_length=50, default="")

    class Meta:
        verbose_name = 'Drone'

    def __str__(self):
        return self.name


class ReasonTable(models.Model):
    reason = models.CharField(max_length=60, default='')

    class Meta:
        verbose_name = 'Reason'

    def __str__(self):
        return self.reason


class MissionTable(models.Model):
    AIRSPACE = [
        ('G', 'Class G'),
        ('A', 'Class A'),
        ('B', 'Class B'),
        ('C', 'Class C'),
        ('D', 'Class D'),
        ('E', 'Class E'),
    ]

    date = models.DateField(default=now(), blank=False)
    time = models.TimeField()
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    pilot = models.ForeignKey(User, on_delete=models.PROTECT, related_name='drone_pilot', null=True)
    observer = models.ForeignKey(User, on_delete=models.PROTECT, related_name='drone_observer', null=True)
    airspace = models.CharField(max_length=1, choices=AIRSPACE, default='G')
    weather = models.CharField(max_length=100, default='')
    wind = models.CharField(max_length=30, default='')
    FAA_Controlling_Agency = models.CharField(max_length=30, default='')
    frequency_used = models.CharField(max_length=10, default='')
    risk_analysis_form_completed = models.BooleanField(default=False)
    NOTAM_Filed = models.BooleanField(default=False)
    NOTAM_Record_Number = models.CharField(max_length=30, default='')
    location = models.CharField(max_length=100, default='')
    case_number_or_CH = models.CharField(max_length=20, blank=True, default='')
    drone_used = models.ManyToManyField(DroneTable)
    total_flight_time = models.FloatField(default=0)
    number_of_flights_flown = models.IntegerField(default=0)
    video_recorded = models.BooleanField(default=True)
    pre_flight_completed_by = models.ForeignKey(User, on_delete=models.PROTECT, related_name='drone_pre', null=True)
    post_flight_completed_by = models.ForeignKey(User, on_delete=models.PROTECT, related_name='drone_post', null=True)

    synopsis_of_events = models.TextField(default="")
    deployment_reason = models.ForeignKey(ReasonTable, on_delete=models.PROTECT)


class DroneLogAttributes(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    has_part107 = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'DroneLogAttributes'


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        DroneLogAttributes.objects.create(user=instance)
    instance.dronelogattributes.save()
