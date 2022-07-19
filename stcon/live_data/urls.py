
from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('logs/', logs, name='logs'),
    path('logs/<int:st_id>/', logs, name='logs_st_id'),
    path('control', control, name='control'),
    path('contacts', contacts, name='contacts'),
    path('help_site', help_site, name='help_site'),
    path('about', about, name='about'),
    path('st/<int:st_id>/', station, name='station'),
    path('st_nm/<int:st_id>/', station_normel, name='station_normel'),
    path('getdata/', getdata, name='getdata'),
    path('getdatanormel/', getdatanormel, name='getdatanormel'),
]