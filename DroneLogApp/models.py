from django.db import models


class DroneTable(models.Model):
    name = models.CharField(max_length=50, default="")
    make = models.CharField(max_length=50, default="")
    model = models.CharField(max_length=50, default="")
    serial = models.CharField(max_length=50, default="")
