from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Part107info(models.Model):
    part107 = models.BooleanField(default=False)


class DroneTable(models.Model):
    name = models.CharField(max_length=50, default="")
    make = models.CharField(max_length=50, default="")
    model = models.CharField(max_length=50, default="")
    serial = models.CharField(max_length=50, default="")


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    part107 = models.ForeignKey(Part107info, on_delete=models.PROTECT, blank=True, null=True)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
