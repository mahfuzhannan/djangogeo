from rest_framework import serializers
from drf_extra_fields.geo_fields import PointField

from geo.models import GeoPoint


class GeoPointSerializer(serializers.ModelSerializer):
    point = PointField(required=False)

    class Meta:
        model = GeoPoint
        fields = '__all__'
