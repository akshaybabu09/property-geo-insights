from django.urls import path

from . import views

urlpatterns = [
    path("", views.CreateListProperties.as_view(), name="create_list_properties"),
    path("<uuid:pk>/", views.RetrieveUpdateProperty.as_view(), name="retrieve_update_property"),
    path("<uuid:property_id>/amenity/", views.CreateListAmenities.as_view(), name="create_list_amenities"),
    path("<uuid:property_id>/amenity/<uuid:pk>/", views.RetrieveUpdateAmenity.as_view(), name="retrieve_update_amenity"),
    path("<uuid:property_id>/surrounding-region/", views.CreateListSurroundingRegion.as_view(), name="create_list_surrounding_region"),
    path("<uuid:property_id>/surrounding-region/<uuid:pk>/", views.RetrieveUpdateSurroundingRegion.as_view(), name="retrieve_update_surrounding_region"),
]
