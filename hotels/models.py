from ckeditor.fields import RichTextField
from django.db import models
from main.models import Hotel


# Create your models here.
class HotelContent(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, blank=True, null=True)
    img = models.ImageField(upload_to="hotel/content/", blank=True, null=True)
    title = models.CharField(max_length=200, blank=True, null=True)
    heading = models.CharField(max_length=200, null=True, blank=True)
    txt = RichTextField(default=None, blank=True, null=True)


class HotelSlider(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, blank=True, null=True)
    img = models.ImageField(upload_to="hotel/slider/", blank=True, null=True)
    txt = RichTextField(default=None, blank=True, null=True)


class Dining(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=500, blank=True, null=True)
    txt = RichTextField(default=None, blank=True, null=True)


class Package(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=200, blank=True, null=True)
    slug = models.SlugField(auto_created=True, unique=True, blank=True, null=True)
    short = models.CharField(max_length=200, blank=True, null=True)
    txt = RichTextField(default=None, blank=True, null=True)
    img = models.ImageField(upload_to="package/", blank=True, null=True)


class Spa(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, blank=True, null=True)
    img = models.ImageField(upload_to="spa/", blank=True, null=True)
    txt = RichTextField(default=None, blank=True, null=True)


class GalleryHotel(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, blank=True, null=True)
    img = models.ImageField(upload_to="hotel/gallery/", blank=True, null=True)
    txt = RichTextField(default=None, null=True, blank=True)


class Location(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, blank=True, null=True)
    location = models.URLField(blank=True, null=True)


class ExploreVenu(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=200, blank=True, null=True)
    img = models.ImageField(upload_to="explore/venu/", blank=True, null=True)
    txt = RichTextField(default=None, blank=True, null=True)


class HotelContact(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, blank=True, null=True)
    txt = RichTextField(default=None, null=True, blank=True)
    img = models.ImageField(upload_to="hotelcontact/", blank=True, null=True)
