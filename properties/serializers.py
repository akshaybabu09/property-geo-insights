from rest_framework_gis.serializers import GeoFeatureModelSerializer

from .models import Property, Amenity, SurroundingRegion


class PropertySerializer(GeoFeatureModelSerializer):

    class Meta:
        model = Property
        geo_field = "boundary"
        fields = ("id", "name", "description", "boundary", "location")
    

class AmenitySerializer(GeoFeatureModelSerializer):

    class Meta:
        model = Amenity
        geo_field = "location"
        fields = ("id", "name", "type", "location", "property")
        read_only_fields = ('property',)


class SurroundingRegionSerializer(GeoFeatureModelSerializer):

    class Meta:
        model = SurroundingRegion
        geo_field = "area"
        fields = ("id", "name", "type", "area", "property")
        read_only_fields = ('property',)
