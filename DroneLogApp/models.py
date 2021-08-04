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
    date = models.DateField(default=now(), blank=False)
    time = models.TimeField()
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    location = models.CharField(max_length=100, default='')
    case_number_or_CH = models.CharField(max_length=20, blank=True, default='')
    drone_used = models.ManyToManyField(DroneTable)
    drone_flight_time = models.FloatField(default=0)
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
