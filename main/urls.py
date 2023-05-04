from django.urls import path
from .views import *

urlpatterns = [
    path('adminpanel', adminpanel, name='adminpanel'),
    path('alllead', alllead, name='alllead'),
    path('slidersection', slidersection, name='slidersection'),
    path('offerslider', offerslider, name='offerslider'),

    # path('addmenu', addmenu, name='addmenu'),
    # path('addubmenu', addubmenu, name='addubmenu'),
    # path('aboutcategory', aboutcategory, name='aboutcategory'),
    # path('eventcategory', eventcategory, name='eventcategory'),

    path('venucategory', venucategory, name='venucategory'),
    path('blogcategory', blogcategory, name='blogcategory'),
    path('venusecatrgory', venusecatrgory, name='venusecatrgory'),
    path('gallerycategory', gallerycategory, name='gallerycategory'),

    path('addvenueslisting', addvenueslisting, name='addvenueslisting'),
    path('viewvenueslisting', viewvenueslisting, name='viewvenueslisting'),
    path('addvenuimages', addvenuimages, name='addvenuimages'),

    path('gallerylist', gallerylist, name='gallerylist'),
    path('videoist', videoist, name='videoist'),
    path('addblog', addblog, name='addblog'),
    path('viewblog', viewblog, name='viewblog'),

    # path('addevents', addevents, name='addevents'),
    # path('viewevents', viewevents, name='viewevents'),
    # path('addtestimonials', addtestimonials, name='addtestimonials'),

    path('addstate', addstate, name='addstate'),
    path('addcity', addcity, name='addcity'),
    # path('addlocation', addlocation, name='addlocation'),
    path('hotel', hotel, name='hotel'),

    # path('add_budget', add_budget, name='add_budget'),
    # path('add_facility', add_facility, name='add_facility'),
    # path('similar_category', similar_category, name='similar_category'),
]
