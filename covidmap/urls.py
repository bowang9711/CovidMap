from django.urls import path
from .views import MarkersMapView
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('db_show',views.db_show,name='db_show'),
    path("map", MarkersMapView.as_view()),
    path('Airline',views.Airline,name='Airline')
    
]