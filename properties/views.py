from rest_framework.generics import RetrieveUpdateAPIView

from .models import Property, Amenity, SurroundingRegion
from .serializers import PropertySerializer, AmenitySerializer, SurroundingRegionSerializer

from library.base_views import BaseListCreateView, NestedListCreateView, BaseNestedRetrieveUpdateView

class CreateListProperties(BaseListCreateView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer

class RetrieveUpdateProperty(RetrieveUpdateAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer

# Amenity views
class CreateListAmenities(NestedListCreateView):
    parent_model = Property
    queryset = Amenity.objects.all()
    serializer_class = AmenitySerializer
    filterset_fields = ["type"]

class RetrieveUpdateAmenity(BaseNestedRetrieveUpdateView):
    queryset = Amenity.objects.all()
    serializer_class = AmenitySerializer

# Surrounding Region views
class CreateListSurroundingRegion(NestedListCreateView):
    parent_model = Property
    queryset = SurroundingRegion.objects.all()
    serializer_class = SurroundingRegionSerializer
    filterset_fields = ["type"]

class RetrieveUpdateSurroundingRegion(BaseNestedRetrieveUpdateView):
    queryset = SurroundingRegion.objects.all()
    serializer_class = SurroundingRegionSerializer