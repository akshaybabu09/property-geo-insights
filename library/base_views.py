from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.exceptions import NotFound
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView



class BaseListCreateView(ListCreateAPIView):
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    search_fields = ["name"]
    ordering_fields = ["id", "created_at", "updated_at"]


class NestedListCreateView(BaseListCreateView):
    parent_model = None
    related_field = "property_id"

    def get_queryset(self):
        parent_id = self.kwargs.get("property_id")
        return self.queryset.filter(**{self.related_field: parent_id})

    def perform_create(self, serializer):
        parent_id = self.kwargs.get("property_id")
        try:
            parent_obj = self.parent_model.objects.get(id=parent_id)
        except self.parent_model.DoesNotExist:
            raise NotFound(f"{self.parent_model.__name__} not found.")
        serializer.save(property=parent_obj)



class BaseNestedRetrieveUpdateView(RetrieveUpdateAPIView):
    lookup_field = "pk"

    def get_queryset(self):
        property_id = self.kwargs.get("property_id")
        return self.queryset.filter(property_id=property_id)