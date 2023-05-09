from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Slider)
admin.site.register(OfferSlider)
# admin.site.register(Menu)
# admin.site.register(SubMenu)
# admin.site.register(AboutCategory)
# admin.site.register(EventCategory)
admin.site.register(BlogCategory)
# admin.site.register(OccasionCategory)
admin.site.register(GalleryCategory)
admin.site.register(GalleryImage)
admin.site.register(GalleryVideo)
admin.site.register(Blog)
admin.site.register(BlogComment)
# admin.site.register(Event)
# admin.site.register(Testimonial)
# admin.site.register(AddBudget)
# admin.site.register(AddFacility)
admin.site.register(Hotel)
admin.site.register(VenuCategory)
admin.site.register(State)
admin.site.register(City)


class VenuAdmin(admin.ModelAdmin):
    list_display = ('id', 'hotel', 'city', 'cat', 'name')
    list_filter = ('hotel', 'state', 'city', 'hotel', 'cat')


admin.site.register(Venu, VenuAdmin)


class VenuImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'venu', 'name')
    list_filter = ('id', 'venu', 'name')


admin.site.register(VenuImages, VenuImageAdmin)
admin.site.register(Reservation)
# admin.site.register()
