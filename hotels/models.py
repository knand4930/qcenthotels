from ckeditor.fields import RichTextField
from django.db import models
from main.models import Hotel


# Create your models here.
class HotelSlider(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, blank=True, null=True)
    img = models.ImageField(upload_to="hotel/slider/", blank=True, null=True)
    txt = RichTextField(default=None, blank=True, null=True)


class Dining(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, blank=True, null=True)
    txt = RichTextField(default=None, blank=True, null=True)


class Package(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=200, blank=True, null=True)
    offer1 = models.CharField(max_length=200, blank=True, null=True)
    offer2 = models.CharField(max_length=200, blank=True, null=True)
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
    address = models.CharField(max_length=200, blank=True, null=True)


class ExploreVenu(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=200, blank=True, null=True)
    img = models.ImageField(upload_to="explore/venu/", blank=True, null=True)
    txt = RichTextField(default=None, blank=True, null=True)


class HotelContact(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    state = models.CharField(max_length=200, blank=True, null=True)
    hotel = models.CharField(max_length=300, blank=True, null=True)
    phone = models.IntegerField(default=None)
    email = models.EmailField(blank=True, null=True, max_length=400)
    txt = models.TextField(default=None)
