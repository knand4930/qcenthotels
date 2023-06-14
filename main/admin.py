from django.contrib import admin
from .models import *
from django.forms import inlineformset_factory

# Register your models here.

admin.site.register(Slider)
admin.site.register(OfferSlider)

admin.site.register(BlogCategory)
admin.site.register(GalleryCategory)
admin.site.register(GalleryImage)
admin.site.register(GalleryVideo)
admin.site.register(Blog)
admin.site.register(BlogComment)
admin.site.register(City)
admin.site.register(Reservation)


class ImageInline(admin.StackedInline):
    model = VenuImages


class VenuAdmin(admin.ModelAdmin):
    inlines = [ImageInline]
    list_display = ('name','hotel')
    list_filter = ('name', 'hotel')


admin.site.register(VenuImages)
admin.site.register(VenuCategory)
# admin.site.register(Hotel)
admin.site.register(Venu, VenuAdmin)
