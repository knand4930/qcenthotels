from django.contrib import admin
from main.models import Hotel
from .models import *


# Register your models here.

class HotelsSliderInline(admin.StackedInline):
    model = HotelSlider


class DiningInline(admin.StackedInline):
    model = Dining


class PackageInline(admin.StackedInline):
    model = Package


class SpaInline(admin.StackedInline):
    model = Spa


class GalleryHotelInline(admin.StackedInline):
    model = GalleryHotel


class LocationInline(admin.StackedInline):
    model = Location


class ExploreVenuInline(admin.StackedInline):
    model = ExploreVenu


class HotelAdmin(admin.ModelAdmin):
    inlines = [HotelsSliderInline, DiningInline, PackageInline, SpaInline, GalleryHotelInline, LocationInline,
               ExploreVenuInline]


admin.site.register(Hotel, HotelAdmin)
