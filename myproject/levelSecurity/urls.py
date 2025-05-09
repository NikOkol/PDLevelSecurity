from django.urls import path
from .views import pd_form_view, gis_form_view, home_view

urlpatterns = [
    path('', home_view, name='home_view'),
    path('pesonal/', pd_form_view, name='pd_form_view'),
    path('gis/', gis_form_view, name='gis_form_view'),
]
