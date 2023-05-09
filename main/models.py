from random import randint

from django.db import models
from django.utils import timezone
from django.utils.html import format_html
from django.utils.text import slugify
from .utils import *
from ckeditor.fields import RichTextField
from account.models import User


# Create your models here.

class Slider(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True, unique=True)
    img = models.ImageField(upload_to='slider/', blank=True, null=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class OfferSlider(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True, unique=True)
    img = models.ImageField(upload_to='slider/', blank=True, null=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


# class Menu(models.Model):
#     title = models.CharField(max_length=200, blank=True, null=True, unique=True)
#     slug = models.SlugField(max_length=300, blank=True, null=True, unique=True)
#     create_at = models.DateTimeField(auto_now_add=True)
#     update_at = models.DateTimeField(auto_now=True)
#
#     def __str__(self):
#         return self.title
#
#     def save(self, *args, **kwargs):
#         if Menu.objects.filter(title=self.title).exists():
#             extra = str(randint(1, 10000))
#             self.slug = slugify(self.title) + "-" + extra
#         else:
#             self.slug = slugify(self.title)
#         super(Menu, self).save(*args, **kwargs)
#
#
# class SubMenu(models.Model):
#     menu = models.ForeignKey(Menu, on_delete=models.CASCADE, blank=True, null=True)
#     title = models.CharField(max_length=200, blank=True, null=True, unique=True)
#     slug = models.SlugField(max_length=300, blank=True, null=True, unique=True)
#     create_at = models.DateTimeField(auto_now_add=True)
#     update_at = models.DateTimeField(auto_now=True)
#
#     def __str__(self):
#         return self.title
#
#     def save(self, *args, **kwargs):
#         if SubMenu.objects.filter(title=self.title).exists():
#             extra = str(randint(1, 10000))
#             self.slug = slugify(self.title) + "-" + extra
#         else:
#             self.slug = slugify(self.title)
#         super(SubMenu, self).save(*args, **kwargs)


# class AboutCategory(models.Model):
#     name = models.CharField(max_length=200, blank=True, null=True, unique=True)
#     slug = models.SlugField(max_length=300, blank=True, null=True, unique=True)
#     txt = models.TextField(blank=True, null=True)
#     icon = models.ImageField(upload_to='aboutcategory/', blank=True, null=True)
#     create_at = models.DateTimeField(auto_now_add=True)
#     update_at = models.DateTimeField(auto_now=True)
#
#     def __str__(self):
#         return self.name
#
#     def save(self, *args, **kwargs):
#         if AboutCategory.objects.filter(name=self.name).exists():
#             extra = str(randint(1, 10000))
#             self.slug = slugify(self.name) + "-" + extra
#         else:
#             self.slug = slugify(self.name)
#         super(AboutCategory, self).save(*args, **kwargs)
#
#
# class EventCategory(models.Model):
#     name = models.CharField(max_length=200, blank=True, null=True, unique=True)
#     slug = models.SlugField(max_length=300, blank=True, null=True, unique=True)
#     txt = models.TextField(blank=True, null=True)
#     icon = models.ImageField(upload_to='eventcategory/', blank=True, null=True)
#     img = models.ImageField(upload_to='eventcategory/', blank=True, null=True)
#     create_at = models.DateTimeField(auto_now_add=True)
#     update_at = models.DateTimeField(auto_now=True)
#
#     def __str__(self):
#         return self.name
#
#     def save(self, *args, **kwargs):
#         if EventCategory.objects.filter(name=self.name).exists():
#             extra = str(randint(1, 10000))
#             self.slug = slugify(self.name) + "-" + extra
#         else:
#             self.slug = slugify(self.name)
#         super(EventCategory, self).save(*args, **kwargs)


class BlogCategory(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True, unique=True)
    slug = models.SlugField(max_length=300, blank=True, null=True, unique=True)
    txt = models.TextField(blank=True, null=True)
    img = models.ImageField(upload_to='blogcategory/', blank=True, null=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if BlogCategory.objects.filter(name=self.name).exists():
            extra = str(randint(1, 10000))
            self.slug = slugify(self.name) + "-" + extra
        else:
            self.slug = slugify(self.name)
        super(BlogCategory, self).save(*args, **kwargs)


class GalleryCategory(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True, unique=True)
    slug = models.SlugField(max_length=300, blank=True, null=True, unique=True)
    img = models.ImageField(upload_to='gallerycategory/', blank=True, null=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if GalleryCategory.objects.filter(name=self.name).exists():
            extra = str(randint(1, 10000))
            self.slug = slugify(self.name) + "-" + extra
        else:
            self.slug = slugify(self.name)
        super(GalleryCategory, self).save(*args, **kwargs)


class GalleryImage(models.Model):
    cat = models.ForeignKey(GalleryCategory, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=200, blank=True, null=True, unique=True)
    slug = models.SlugField(max_length=300, blank=True, null=True, unique=True)
    img = models.ImageField(upload_to="galleryimage/", blank=True, null=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if GalleryImage.objects.filter(title=self.title).exists():
            extra = str(randint(1, 10000))
            self.slug = slugify(self.title) + "-" + extra
        else:
            self.slug = slugify(self.title)
        super(GalleryImage, self).save(*args, **kwargs)


class GalleryVideo(models.Model):
    cat = models.ForeignKey(GalleryCategory, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=200, blank=True, null=True, unique=True)
    slug = models.SlugField(max_length=300, blank=True, null=True, unique=True)
    lnk = models.TextField(blank=True, null=True)
    file = models.FileField(upload_to="galleryvideo/", blank=True, null=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if GalleryVideo.objects.filter(title=self.title).exists():
            extra = str(randint(1, 10000))
            self.slug = slugify(self.title) + "-" + extra
        else:
            self.slug = slugify(self.title)
        super(GalleryVideo, self).save(*args, **kwargs)


class Blog(models.Model):
    cat = models.ForeignKey(BlogCategory, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=500, blank=True, null=True, unique=True)
    slug = models.SlugField(max_length=600, blank=True, null=True, unique=True)
    caption = models.TextField(blank=True, null=True)
    meta_title = models.TextField(blank=True, null=True)
    meta_keyword = models.TextField(blank=True, null=True)
    meta_description = models.TextField(blank=True, null=True)
    img = models.ImageField(upload_to='blog/', blank=True, null=True)
    txt = RichTextField(blank=True, null=True)
    view = models.PositiveBigIntegerField(default=0)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if Blog.objects.filter(title=self.title).exists():
            extra = str(randint(1, 10000))
            self.slug = slugify(self.title) + "-" + extra
        else:
            self.slug = slugify(self.title)
        super(Blog, self).save(*args, **kwargs)

    @property
    def number_of_comments(self):
        return BlogComment.objects.filter(blog=self).count()


class BlogComment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    create_at = models.DateTimeField(auto_now_add=True)


# class Event(models.Model):
#     cat = models.ForeignKey(EventCategory, on_delete=models.CASCADE, blank=True, null=True)
#     title = models.CharField(max_length=500, blank=True, null=True, unique=True)
#     slug = models.SlugField(max_length=600, blank=True, null=True, unique=True)
#     caption = models.TextField(blank=True, null=True)
#     img = models.ImageField(upload_to='blog/', blank=True, null=True)
#     txt = RichTextField(blank=True, null=True)
#     create_at = models.DateTimeField(auto_now_add=True)
#     update_at = models.DateTimeField(auto_now=True)
#
#     def __str__(self):
#         return self.title
#
#     def save(self, *args, **kwargs):
#         if Event.objects.filter(title=self.title).exists():
#             extra = str(randint(1, 10000))
#             self.slug = slugify(self.title) + "-" + extra
#         else:
#             self.slug = slugify(self.title)
#         super(Event, self).save(*args, **kwargs)


# class Testimonial(models.Model):
#     name = models.CharField(max_length=200, blank=True, null=True, unique=True)
#     slug = models.SlugField(max_length=200, blank=True, null=True, unique=True)
#     postion = models.CharField(max_length=200, blank=True, null=True)
#     img = models.ImageField(upload_to='testimonial/', blank=True, null=True)
#     txt = RichTextField(blank=True, null=True)
#     create_at = models.DateTimeField(auto_now_add=True)
#     update_at = models.DateTimeField(auto_now=True)
#
#     def __str__(self):
#         return self.name
#
#     def save(self, *args, **kwargs):
#         if Testimonial.objects.filter(name=self.name).exists():
#             extra = str(randint(1, 10000))
#             self.slug = slugify(self.name) + "-" + extra
#         else:
#             self.slug = slugify(self.name)
#         super(Testimonial, self).save(*args, **kwargs)


class VenuCategory(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True, unique=True)
    slug = models.SlugField(max_length=300, blank=True, null=True, unique=True)
    img = models.ImageField(upload_to="vanu/category/", blank=True, null=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if VenuCategory.objects.filter(name=self.name).exists():
            extra = str(randint(1, 10000))
            self.slug = slugify(self.name) + "-" + extra
        else:
            self.slug = slugify(self.name)
        super(VenuCategory, self).save(*args, **kwargs)


class State(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    slug = models.SlugField(max_length=300, blank=True, null=True, unique=True)
    create_at = models.DateTimeField(auto_now_add=True)
    udpate_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if State.objects.filter(name=self.name).exists():
            extra = str(randint(1, 10000))
            self.slug = slugify(self.name) + "-" + extra
        else:
            self.slug = slugify(self.name)
        super(State, self).save(*args, **kwargs)


# class Location(models.Model):
#     name = models.CharField(max_length=200, blank=True, null=True, unique=True)
#     slug = models.SlugField(max_length=300, blank=True, null=True, unique=True)
#     create_at = models.DateTimeField(auto_now_add=True)
#     udpate_at = models.DateTimeField(auto_now=True)
#
#     def __str__(self):
#         return self.name
#
#     def save(self, *args, **kwargs):
#         if Location.objects.filter(name=self.name).exists():
#             extra = str(randint(1, 10000))
#             self.slug = slugify(self.name) + "-" + extra
#         else:
#             self.slug = slugify(self.name)
#         super(Location, self).save(*args, **kwargs)


class City(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    slug = models.SlugField(max_length=300, blank=True, null=True, unique=True)
    create_at = models.DateTimeField(auto_now_add=True)
    udpate_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if City.objects.filter(name=self.name).exists():
            extra = str(randint(1, 10000))
            self.slug = slugify(self.name) + "-" + extra
        else:
            self.slug = slugify(self.name)
        super(City, self).save(*args, **kwargs)


# class SimilarCategory(models.Model):
#     name = models.CharField(max_length=200, blank=True, null=True)
#     slug = models.SlugField(max_length=300, blank=True, null=True, unique=True)
#     create_at = models.DateTimeField(auto_now_add=True)
#     udpate_at = models.DateTimeField(auto_now=True)
#
#     def __str__(self):
#         return self.name
#
#     def save(self, *args, **kwargs):
#         if SimilarCategory.objects.filter(name=self.name).exists():
#             extra = str(randint(1, 10000))
#             self.slug = slugify(self.name) + "-" + extra
#         else:
#             self.slug = slugify(self.name)
#         super(SimilarCategory, self).save(*args, **kwargs)


# class AddBudget(models.Model):
#     name = models.CharField(max_length=200, blank=True, null=True)
#     slug = models.SlugField(max_length=300, blank=True, null=True, unique=True)
#     create_at = models.DateTimeField(auto_now_add=True)
#     udpate_at = models.DateTimeField(auto_now=True)
#
#     def __str__(self):
#         return self.name
#
#     def save(self, *args, **kwargs):
#         if AddBudget.objects.filter(name=self.name).exists():
#             extra = str(randint(1, 10000))
#             self.slug = slugify(self.name) + "-" + extra
#         else:
#             self.slug = slugify(self.name)
#         super(AddBudget, self).save(*args, **kwargs)


# class AddFacility(models.Model):
#     name = models.CharField(max_length=200, blank=True, null=True)
#     slug = models.SlugField(max_length=300, blank=True, null=True, unique=True)
#     create_at = models.DateTimeField(auto_now_add=True)
#     udpate_at = models.DateTimeField(auto_now=True)
#
#     def __str__(self):
#         return self.name
#
#     def save(self, *args, **kwargs):
#         if AddFacility.objects.filter(name=self.name).exists():
#             extra = str(randint(1, 10000))
#             self.slug = slugify(self.name) + "-" + extra
#         else:
#             self.slug = slugify(self.name)
#         super(AddFacility, self).save(*args, **kwargs)


class Hotel(models.Model):
    state = models.ForeignKey(State, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    img = models.ImageField(upload_to="hotel/", blank=True, null=True)
    summary = models.TextField(default=None, blank=True, null=True)
    slug = models.SlugField(max_length=300, blank=True, null=True, unique=True)
    create_at = models.DateTimeField(auto_now_add=True)
    udpate_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if Hotel.objects.filter(name=self.name).exists():
            extra = str(randint(1, 10000))
            self.slug = slugify(self.name) + "-" + extra
        else:
            self.slug = slugify(self.name)
        super(Hotel, self).save(*args, **kwargs)


class Venu(models.Model):
    cat = models.ForeignKey(VenuCategory, on_delete=models.CASCADE, blank=True, null=True)
    state = models.ForeignKey(State, on_delete=models.CASCADE, blank=True, null=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE, blank=True, null=True)
    # location = models.ForeignKey(Location, on_delete=models.CASCADE, blank=True, null=True)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, blank=True, null=True)
    # facility = models.ForeignKey(AddFacility, on_delete=models.CASCADE, blank=True, null=True)

    budget = models.PositiveBigIntegerField(blank=True, null=True)
    price_increase = models.PositiveBigIntegerField(blank=True, null=True)
    agent_price = models.PositiveBigIntegerField(blank=True, null=True)
    total_budget = models.PositiveBigIntegerField(blank=True, null=True)
    agent = models.PositiveBigIntegerField(blank=True, null=True)

    name = models.CharField(max_length=200, blank=True, null=True)
    slug = models.SlugField(max_length=300, blank=True, null=True, unique=True)
    address = models.CharField(max_length=500, blank=True, null=True)

    parking = models.BooleanField("Parking", default=False, blank=True, null=True)
    wifi = models.BooleanField("Wi Fi", default=False, blank=True, null=True)
    breakfast = models.BooleanField("Break Fast", default=False, blank=True, null=True)
    pool = models.BooleanField("Swiming Pool", default=False, blank=True, null=True)
    reception = models.BooleanField(default=False, blank=True, null=True)
    gym = models.BooleanField(default=False, blank=True, null=True)

    # phone = models.IntegerField(blank=True, null=True)
    # email = models.EmailField(max_length=200, blank=True, null=True)
    # veg_plate = models.CharField(max_length=200, blank=True, null=True)
    # non_veg_plate = models.CharField(max_length=200, blank=True, null=True)
    # min_capacity = models.CharField(max_length=200, blank=True, null=True)
    # max_capacity = models.CharField(max_length=200, blank=True, null=True)
    # meta_title = models.CharField(max_length=200, blank=True, null=True)
    # meta_keyword = models.CharField(max_length=200, blank=True, null=True)
    # meta_description = models.CharField(max_length=200, blank=True, null=True)
    img = models.ImageField(upload_to='venue/', blank=True, null=True)

    # venue_policy = models.TextField(blank=True, null=True)
    summary = models.TextField(blank=True, null=True)
    alcohol = models.TextField(blank=True, null=True)
    food = models.TextField(blank=True, null=True)
    decoration = models.TextField(blank=True, null=True)

    advance = models.CharField(max_length=200, blank=True, null=True)
    cancelecation_charge = models.CharField(max_length=200, blank=True, null=True)
    parking_at = models.CharField(max_length=200, blank=True, null=True)
    taxes_charge = models.CharField(max_length=200, blank=True, null=True)

    check_in = models.TimeField(blank=True, null=True)
    check_out = models.TimeField(blank=True, null=True)

    #
    # start_time_morning = models.TimeField(blank=True, null=True)
    # end_time_morning = models.TimeField(blank=True, null=True)
    # start_time_evening = models.TimeField(blank=True, null=True)
    # end_time_evening = models.TimeField(blank=True, null=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if Venu.objects.filter(name=self.name).exists():
            extra = str(randint(1, 10000))
            self.slug = slugify(self.name) + "-" + extra
        else:
            self.slug = slugify(self.name)
        super(Venu, self).save(*args, **kwargs)


class VenuImages(models.Model):
    venu = models.ForeignKey(Venu, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    img = models.ImageField(upload_to="venu/images/")

    def __str__(self):
        return self.name



#
# class VenuCategory(models.Model):
#     name = models.CharField(max_length=200, blank=True, null=True)
#     slug = models.SlugField(max_length=300, blank=True, null=True)
#     create_at = models.DateTimeField(auto_now_add=True)
#     update_at = models.DateTimeField(auto_now=True)
#
#     def save(self, *args, **kwargs):
#         if VenuCategory.objects.filter(name=self.name).exists():
#             extra = str(randint(1, 10000))
#             self.slug = slugify(self.name) + "-" + extra
#         else:
#             self.slug = slugify(self.name)
#         super(VenuCategory, self).save(*args, **kwargs)


class Reservation(models.Model):
    STATUS_CHOICE = (
        ('pending', 'pending'),
        ('accepted', 'accepted'),
        ('cancelled', 'cancelled'),
        ('completed', 'completed'),
    )
    """Models for reservations"""
    reservation_id = models.CharField(max_length=200, blank=True, null=True, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hotel = models.ForeignKey(Venu, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    mobile = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=200, blank=True, null=True)
    children = models.PositiveSmallIntegerField(default=0)
    guest = models.PositiveSmallIntegerField(default=1)
    room = models.PositiveSmallIntegerField(default=1)
    check_in = models.DateField(blank=True, null=True)
    check_out = models.DateField(blank=True, null=True)
    price = models.PositiveBigIntegerField(blank=True, null=True)
    user_type = models.CharField(max_length=200, blank=True, null=True)
    status = models.CharField(max_length=200, blank=True, null=True, default='pending', choices=STATUS_CHOICE)

    def __str__(self):
        return self.name


