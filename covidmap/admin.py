from django.contrib.gis import admin

from .models import Marker

# Register your models here.
from .models import Covidinfor

admin.site.register(Covidinfor)

@admin.register(Marker)
class MarkerAdmin(admin.OSMGeoAdmin):
    """Marker admin."""

    list_display = ("name", "location")