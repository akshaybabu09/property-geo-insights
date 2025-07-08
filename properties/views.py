from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from rest_framework.exceptions import NotFound

from .models import Property, Amenity, SurroundingRegion
from .serializers import PropertySerializer, AmenitySerializer, SurroundingRegionSerializer

# Create your views here.

class CreateListProperties(ListCreateAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer


class RetrieveUpdateProperty(RetrieveUpdateAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer


class CreateListAmenities(ListCreateAPIView):
    queryset = Amenity.objects.all()
    serializer_class = AmenitySerializer

    def get_queryset(self):
        property_id = self.kwargs.get("property_id")
        return Amenity.objects.filter(property_id=property_id)

    def perform_create(self, serializer):
        property_id = self.kwargs.get("property_id")
        try:
            property_obj = Property.objects.get(id=property_id)
        except Property.DoesNotExist:
            raise NotFound("Property not found.")

        serializer.save(property=property_obj)


class RetrieveUpdateAmenity(RetrieveUpdateAPIView):
    serializer_class = AmenitySerializer
    lookup_field = 'pk'

    def get_queryset(self):
        property_id = self.kwargs.get("property_id")
        return Amenity.objects.filter(property_id=property_id)


class CreateListSurroundingRegion(ListCreateAPIView):
    serializer_class = SurroundingRegionSerializer

    def get_queryset(self):
        property_id = self.kwargs.get("property_id")
        return SurroundingRegion.objects.filter(property_id=property_id)

    def perform_create(self, serializer):
        property_id = self.kwargs.get("property_id")
        try:
            property_obj = Property.objects.get(id=property_id)
        except Property.DoesNotExist:
            raise NotFound("Property not found.")

        serializer.save(property=property_obj)


class RetrieveUpdateSurroundingRegion(RetrieveUpdateAPIView):
    serializer_class = SurroundingRegionSerializer
    lookup_field = "pk"
    
    def get_queryset(self):
        property_id = self.kwargs.get("property_id")
        return SurroundingRegion.objects.filter(property_id=property_id)
