from django.urls import path
from .views import *

urlpatterns = [
    path('roomlist/<slug:slug>/', roomlist, name='roomlist'),
    path('hoteldining/<slug:slug>/', hoteldining, name='hoteldining'),
    path('hotelspa/<slug:slug>/', hotelspa, name='hotelspa'),
    path('hotelgallery/<slug:slug>/', hotelgallery, name='hotelgallery'),
    path('hotellocation/<slug:slug>/', hotellocation, name='hotellocation'),
    path('hotelvenue/<slug:slug>/', hotelvenue, name='hotelvenue'),
    path('hotelcontact/<slug:slug>/', hotelcontact, name='hotelcontact'),
    path('hotelpackage/<slug:slug>/', hotelpackage, name='hotelpackage'),
    path('packagedetails/<slug:slug>/<int:id>/', packagedetails, name='packagedetails'),
    path('explorevenu/<slug:slug>/<int:id>/', explorevenu, name='explorevenu'),
]
