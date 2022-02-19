from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
# from django.shortcuts import render_to_response
from .models import Covidinfor
from django.views.generic.base import TemplateView
import json
from django.core.serializers import serialize
from .models import Marker

# Create your views here.

def index(request):
    return render(request, 'index.html')

def Airline(request):
    return render(request, 'Airline.html')


def db_show(request):
    user_list_obj = Covidinfor.objects.all()
    return render(request, 'db_show.html', {'li': user_list_obj})
    # return render_to_response("db_show.html",locals())


class MarkersMapView(TemplateView):
    """Markers map view."""

    template_name = "map.html"
    
    def get_context_data(self, **kwargs):
        """Return the view context data."""
        context = super().get_context_data(**kwargs)
        context["markers"] = json.loads(serialize("geojson", Marker.objects.all()))
        return context
