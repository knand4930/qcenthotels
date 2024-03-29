from django.http import HttpResponseNotFound
from django.shortcuts import render, get_object_or_404, redirect
from main.models import Hotel, Venu, State, VenuCategory
from account.models import *
from .models import *


# Create your views here.


def roomlist(request, slug):
    hotels = get_object_or_404(Hotel, slug=slug)
    room = Venu.objects.filter(hotel=hotels)
    state = State.objects.all()
    cat = VenuCategory.objects.all()[:1]
    return render(request, 'roomlist.html', {'hotels': hotels, 'room': room, 'state': state, 'cat': cat})


def hoteldining(request, slug):
    hotels = get_object_or_404(Hotel, slug=slug)
    din = Dining.objects.filter(hotel=hotels)
    slider = HotelSlider.objects.filter(hotel=hotels)
    state = State.objects.all()
    cat = VenuCategory.objects.all()[:1]
    return render(request, 'hoteldining.html',
                  {'hotels': hotels, 'din': din, 'state': state, 'cat': cat, 'slider': slider})


def hotelpackage(request, slug):
    hotels = get_object_or_404(Hotel, slug=slug)
    package = Package.objects.filter(hotel=hotels)
    state = State.objects.all()
    cat = VenuCategory.objects.all()[:1]
    return render(request, 'hotelpackage.html', {'hotels': hotels, 'package': package, 'state': state, 'cat': cat})


def hotelspa(request, slug):
    hotels = get_object_or_404(Hotel, slug=slug)
    sp = Spa.objects.filter(hotel=hotels)
    state = State.objects.all()
    cat = VenuCategory.objects.all()[:1]
    return render(request, 'hotelspa.html', {'hotels': hotels, 'sp': sp, 'state': state, 'cat': cat})


def hotelgallery(request, slug):
    hotels = get_object_or_404(Hotel, slug=slug)
    gh = GalleryHotel.objects.filter(hotel=hotels)
    state = State.objects.all()
    cat = VenuCategory.objects.all()[:1]
    return render(request, 'hotelgallery.html', {'hotels': hotels, 'gh': gh, 'state': state, 'cat': cat})


def hotellocation(request, slug):
    hotels = get_object_or_404(Hotel, slug=slug)
    loc = Location.objects.filter(hotel=hotels)[:1]
    state = State.objects.all()
    cat = VenuCategory.objects.all()[:1]
    return render(request, 'hotellocation.html', {'hotels': hotels, 'loc': loc, 'state': state, 'cat': cat})


def hotelvenue(request, slug):
    hotels = get_object_or_404(Hotel, slug=slug)
    expvenu = ExploreVenu.objects.filter(hotel=hotels)
    state = State.objects.all()
    cat = VenuCategory.objects.all()[:1]
    return render(request, 'hotelvenue.html', {'hotels': hotels, 'expvenu': expvenu, 'state': state, 'cat': cat})


def hotelcontact(request, slug):
    hotels = get_object_or_404(Hotel, slug=slug)
    state = State.objects.all()
    cat = VenuCategory.objects.all()[:1]
    address = HotelContact.objects.filter(hotel=hotels)[:1]
    return render(request, 'hotelcontact.html', {'hotels': hotels, 'state': state, 'cat': cat, 'address':address})


def packagedetails(request, slug, id):
    hotels = get_object_or_404(Hotel, slug=slug)
    cat = VenuCategory.objects.all()[:1]
    state = State.objects.all()
    package = Package.objects.get(id=id)
    return render(request, 'package.html', {'package': package, 'cat':cat, 'state':state, 'hotels':hotels})


def explorevenu(request, slug, id):
    hotels = get_object_or_404(Hotel, slug=slug)
    cat = VenuCategory.objects.all()[:1]
    state = State.objects.all()
    exp = get_object_or_404(ExploreVenu, id=id)
    return render(request, 'explorevenu.html', {'exp': exp, 'cat':cat, 'state':state, 'hotels':hotels})
