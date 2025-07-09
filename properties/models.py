import uuid
from django.db import models
from django.contrib.gis.db import models

from library.base_models import TimeStampedModel


# Create your models here.
class AmenityType(models.TextChoices):
    SCHOOL = "SCHOOL", "School"
    HOSPITAL = "HOSPITAL", "Hospital"
    MALL = "MALL", "Mall"
    SUPERMARKET = "SUPERMARKET", "Super Market"


class RegionType(models.TextChoices):
    LAKE = "LAKE", "Lake"
    PARK = "PARK", "Park"
    INDUSTRIAL_AREA = "INDUSTRIAL_AREA", "Industrial Area"
    TREATMENT_PLANT = "TREATMENT_PLANT", "Treatment Plant"


class Property(TimeStampedModel):
    """
        Model to store the properties with name, address, description, location and boundary
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=256)
    description = models.TextField(null=True, blank=True)
    address = models.TextField()
    location = models.PointField()
    boundary = models.PolygonField()

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Properties"
        constraints = [
                models.UniqueConstraint(
                    fields=["location", "boundary"],
                    name="unique_property_location_and_boundary"
                )
            ]


class Amenity(TimeStampedModel):
    """
        Model to store the list of Schools, Hospitals, Malls, Grocery Stores / Super markets etc.,
        in the neighboudhood of the property.

        We have made an assumption that each place is a distinct entity with its own set of metadata 
        such as name, type, distance. This will help us in writing optimized queries to find list of 
        schools and hospitals within 5km.
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=256)
    type = models.CharField(max_length=16, choices=AmenityType)
    location = models.PointField()
    property = models.ForeignKey("Property", related_name="amenities", on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Amenities"
        constraints = [
            models.UniqueConstraint(
                fields=["type", "location"],
                name="unique_amenity_type_and_location"
            )
        ]


class SurroundingRegion(TimeStampedModel):
    """
        Model to store the list of Parks, Lakes, Cemetary, Industrial Areas, Treatment Plants
         in the vicinity of the property.

        We have made an assumption the areas are continuous and since each of the areas have its own 
        set of metadata we are storing individually. We can use MultiPolygonField when we are dealing with
        disconnected pieces of areas such as National Parks or Reserved Forests.
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=256)
    type = models.CharField(max_length=16, choices=RegionType)
    area = models.PolygonField()
    property = models.ForeignKey("Property", related_name="surronding_regions", on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    class Meta:
        constraints = [
                models.UniqueConstraint(
                    fields=["type", "area"],
                    name="unique_amenity_type_and_area"
                )
            ]

