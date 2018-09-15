from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from geo.models import GeoPoint
from geo.serializers import GeoPointSerializer


class GeoPointViewSet(viewsets.ModelViewSet):
    queryset = GeoPoint.objects.all()
    serializer_class = GeoPointSerializer