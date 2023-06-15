from django.contrib import admin
from main.models import Hotel
from .models import *
from import_export.admin import ImportExportModelAdmin


# Register your models here.
class HotelContentInline(admin.StackedInline):
    model = HotelContent


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


class HotelContactInline(admin.StackedInline):
    model = HotelContact


class HotelAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    inlines = [HotelContentInline, HotelsSliderInline, DiningInline, PackageInline, SpaInline, GalleryHotelInline,
               LocationInline,
               ExploreVenuInline, HotelContactInline]
    list_display = ('name', 'state', 'cat', 'city')


admin.site.register(Hotel, HotelAdmin)



