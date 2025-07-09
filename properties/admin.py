from django.contrib import admin

from .models import Property, Amenity, SurroundingRegion

# Register your models here.

class PropertyAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "address"
    )
    readonly_fields = ["id", "created_at", "updated_at"]

class AmenityAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "type",
        "property",
    )
    list_filter = ("type",)
    readonly_fields = ["id", "created_at", "updated_at"]

class SurroundingRegionAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "type",
        "property"
    )
    list_filter = ("type",)
    readonly_fields = ["id", "created_at", "updated_at"]

admin.site.register(Property, PropertyAdmin)
admin.site.register(Amenity, AmenityAdmin)
admin.site.register(SurroundingRegion, SurroundingRegionAdmin)
