from django.urls import path

from . import views

urlpatterns = [
    path("", views.CreateListProperties.as_view(), name="create-list-properties"),
    path("<uuid:pk>/", views.RetrieveUpdateProperty.as_view(), name="retrieve-update-property"),
    path("<uuid:property_id>/amenity/", views.CreateListAmenities.as_view(), name="create-list-amenities"),
    path("<uuid:property_id>/amenity/<uuid:pk>/", views.RetrieveUpdateAmenity.as_view(), name="retrieve-update-amenity"),
    path("<uuid:property_id>/surrounding-region/", views.CreateListSurroundingRegion.as_view(), name="create-list-surrounding-region"),
    path("<uuid:property_id>/surrounding-region/<uuid:pk>/", views.RetrieveUpdateSurroundingRegion.as_view(), name="retrieve-update-surrounding-region"),
]
