from django.contrib.gis.db import models

# Create your models here.


class GeoPoint(models.Model):
    point = models.PointField()