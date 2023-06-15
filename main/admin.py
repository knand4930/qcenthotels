from django.contrib import admin
from .models import *
from django.forms import inlineformset_factory
from import_export.admin import ImportExportModelAdmin
from import_export import resources


# Register your models here.

class SliderAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('title', 'create_at')


admin.site.register(Slider, SliderAdmin)


class OfferSliderAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('title', 'create_at')


admin.site.register(OfferSlider, OfferSliderAdmin)


class BlogCategoryAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('name', 'create_at')


admin.site.register(BlogCategory, BlogCategoryAdmin)


class GalleryCategoryAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('name', 'create_at')


admin.site.register(GalleryCategory, GalleryCategoryAdmin)


class GalleryImageAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('title', 'create_at')


admin.site.register(GalleryImage, GalleryImageAdmin)


class GalleryVideoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('title', 'create_at')


admin.site.register(GalleryVideo, GalleryVideoAdmin)


class BlogAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('title', 'create_at')


admin.site.register(Blog)


class BlogCommentAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('blog', 'create_at')


admin.site.register(BlogComment, BlogCommentAdmin)


class CityAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('name', 'create_at')


admin.site.register(City, CityAdmin)


class ReservationAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('name', 'mobile')


admin.site.register(Reservation, ReservationAdmin)


class ImageInline(admin.StackedInline):
    model = VenuImages


class VenuAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    inlines = [ImageInline]
    list_display = ('name', 'hotel')
    list_filter = ('name', 'hotel')


admin.site.register(Venu, VenuAdmin)


class VenuCategoryAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('name', 'create_at')


admin.site.register(VenuCategory, VenuCategoryAdmin)


# admin.site.register(Hotel)

class VenuImageAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'name', 'venu')


admin.site.register(VenuImages, VenuImageAdmin)
