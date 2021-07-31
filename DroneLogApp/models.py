from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class DroneTable(models.Model):
    name = models.CharField(max_length=50, default="")
    make = models.CharField(max_length=50, default="")
    model = models.CharField(max_length=50, default="")
    serial = models.CharField(max_length=50, default="")


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    has_part107 = models.BooleanField(default=False)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

