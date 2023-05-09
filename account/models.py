from ckeditor.fields import RichTextField
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils import timezone


# Create your models here.
class User(AbstractUser):
    phone = models.PositiveBigIntegerField(blank=True, null=True)
    country_code = models.CharField(max_length=10, blank=True, null=True)
    is_customer = models.BooleanField("Is Customer", default=False)
    is_agent = models.BooleanField("Is Agent", default=False)


class Profile(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True)
    first_name = models.CharField(max_length=200, blank=True, null=True)
    last_name = models.CharField(max_length=200, blank=True, null=True)
    city = models.CharField(max_length=200, blank=True, null=True)
    state = models.CharField(max_length=200, blank=True, null=True)
    zip_code = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(max_length=200, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    address = models.TextField(default=None, blank=True, null=True)


class ContactUs(models.Model):
    first_name = models.CharField(max_length=200, blank=True, null=True)
    last_name = models.CharField(max_length=200, blank=True, null=True)
    email = models.CharField(max_length=200, blank=True, null=True)
    phone = models.CharField(max_length=200, blank=True, null=True)
    msg = models.TextField(blank=True, null=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)


# https://github.com/anisbhsl/Hotel-Management-System/blob/master/main/models.py

# class Reservation(models.Model):
#     STATUS_CHOICE = (
#         ('pending', 'pending'),
#         ('accepted', 'accepted'),
#         ('cancelled', 'cancelled'),
#         ('completed', 'completed'),
#     )
#     """Models for reservations"""
#     reservation_id = models.AutoField(primary_key=True)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     hotel = models.ForeignKey(Venu, on_delete=models.CASCADE, blank=True, null=True)
#     no_of_children = models.PositiveSmallIntegerField(default=0)
#     no_of_adults = models.PositiveSmallIntegerField(default=1)
#     no_of_rooms = models.PositiveSmallIntegerField(default=1)
#     reservation_date_time = models.DateTimeField(default=timezone.now)
#     expected_arrival_date_time = models.DateTimeField(default=timezone.now)
#     expected_departure_date_time = models.DateTimeField(default=timezone.now)
#     status = models.CharField(max_length=200, blank=True, null=True, default='pending', choices=STATUS_CHOICE)
#
#     class Meta:
#         permissions = (('can_view_reservation', 'Can view reservation'),
#                        ('can_view_reservation_detail', 'Can view reservation detail'),)
#
#     def get_absolute_url(self):
#         return reverse('reservation-detail', args=str([self.reservation_id]))
#
#     def __str__(self):
#         return '({0}) {1} {2}'.format(self.reservation_id, self.customer.first_name, self.customer.last_name)


# class CancelletionRefund(models.Model):
#     STATUS_CHOICE = (
#         ('cancel', 'cancel'),
#         ('review',  'review'),
#         ('profile', 'profile'),
#         ('report', 'report'),
#         ('support', 'support'),
#     )
#     reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE, blank=True, null=True)
#     user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
#     status = models.CharField(max_length=200, blank=True, null=True, default='cancel', choices=STATUS_CHOICE)
#
# class Room(models.Model):
#     room_no = models.CharField(max_length=10, primary_key=True)
#     room_type = models.ForeignKey('RoomType', null=False, blank=True, on_delete=models.CASCADE)
#     availability = models.BooleanField(default=0)
#     reservation = models.ForeignKey(Reservation, null=True, blank=True, on_delete=models.SET_NULL)
#     facility = models.ManyToManyField('Facility')
#
#     class Meta:
#         ordering = ['room_no', ]
#         permissions = (('can_view_room', 'Can view room'),)
#
#     def __str__(self):
#         return "%s - %s - Rs. %i" % (self.room_no, self.room_type.name, self.room_type.price)
#
#     def display_facility(self):
#         """
#         This function should be defined since facility is many-to-many relationship
#         It cannot be displayed directly on the admin panel for list_display
#         """
#         return ', '.join([facility.name for facility in self.facility.all()])
#
#     display_facility.short_description = 'Facilities'
#
#     def get_absolute_url(self):
#         return reverse('room-detail', args=[self.room_no])
#
#     def save(self, *args, **kwargs):  # Overriding default behaviour of save
#         if self.reservation:  # If it is reserved, then it should not be available
#             self.availability = 0
#         else:
#             self.availability = 1
#
#         super().save(*args, **kwargs)
#
#
# class Facility(models.Model):
#     name = models.CharField(max_length=25)
#     price = models.PositiveSmallIntegerField()
#
#     class Meta:
#         verbose_name_plural = 'Facilities'  # Otherwise admin panel shows Facilitys
#
#     def __str__(self):
#         return self.name
#

class RoomType(models.Model):
    name = models.CharField(max_length=25)
    price = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.name


class Career(models.Model):
    fname = models.CharField(max_length=200, blank=True, null=True)
    mobile = models.IntegerField(blank=True, null=True)
    position = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(max_length=300, blank=True, null=True)
    cv = models.FileField(upload_to="cv/", blank=True, null=True)
    msg = models.TextField(default=None)

    def __str__(self):
        return self.fname


class MarriageEvents(models.Model):
    bride_groom = models.CharField(max_length=500, blank=True, null=True)
    function = models.CharField(max_length=500, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    time = models.TimeField(blank=True, null=True)
    number_of_room = models.CharField(max_length=500, blank=True, null=True)
    location = models.CharField(max_length=500, blank=True, null=True)
    guest_capacity = models.CharField(max_length=500, blank=True, null=True)
    number_of_night = models.CharField(max_length=500, blank=True, null=True)
    contact_number = models.CharField(max_length=500, blank=True, null=True)
    email_address = models.CharField(max_length=500, blank=True, null=True)
    msg = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.bride_groom


class Partner(models.Model):
    fname = models.CharField(max_length=300, blank=True, null=True)
    hotel_name = models.CharField(max_length=300, blank=True, null=True)
    mobile = models.CharField(max_length=300, blank=True, null=True)
    address = models.CharField(max_length=300, blank=True, null=True)
    email = models.CharField(max_length=300, blank=True, null=True)
    room = models.CharField(max_length=300, blank=True, null=True)
    msg = models.CharField(max_length=300, blank=True, null=True)

    def __str__(self):
        return self.fname


class EventText(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    desc = RichTextField(blank=True, null=True, default=None)


class EventSlider(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    img = models.ImageField(upload_to="EventSlider/", blank=True, null=True)
