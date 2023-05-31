from django.contrib.auth import logout, authenticate, login
from django.core.paginator import PageNotAnInteger, EmptyPage, Paginator
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from main.models import *
from .serializers import HotelSerializers
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView
import django_filters


# Create your views here.
def home(request):
    blg = Blog.objects.all()
    cat = VenuCategory.objects.all()[:1]
    city = City.objects.all()
    state = State.objects.all()
    # location = Location.objects.all()
    related = Hotel.objects.all()
    # budget = AddBudget.objects.all()
    # facility = AddFacility.objects.all()
    # sm_cat = SimilarCategory.objects.all()
    slider = Slider.objects.all()
    venu = Venu.objects.all()
    offer = OfferSlider.objects.all()
    hme = Hotel.objects.all()[:6]
    #   hotel = Hotels.objects.all()[:3]
    context = {'cat': cat, 'city': city, 'related': related, 'venu': venu,
               'state': state, 'blg': blg, 'hme': hme, 'slider': slider}
    return render(request, 'home.html', context)


def login_attempt(request):
    state = State.objects.all()
    cat = VenuCategory.objects.all()[:1]
    try:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user_obj = User.objects.filter(username=username).first()

            if user_obj is None:
                msg = "User Not Found !"
                return render(request, 'login_attempt.html', {'msg': msg})

            user = authenticate(username=username, password=password)
            if user is None:
                msg = "Password Error !"
                return render(request, 'login_attempt.html', {'msg': msg})

            if user is not None:
                if user.is_superuser:
                    login(request, user)
                    return redirect('adminpanel')
                elif user.is_authenticated or user.is_agent or user.is_customer:
                    login(request, user)
                    return redirect('/')
                else:
                    msg = "Something Went Wrong Please contact with Administrator !"
                    return render(request, 'login_attempt.html', {'msg': msg})
            else:
                msg = "Something Went Wrong Please contact with Administrator !"
                return render(request, 'login_attempt.html', {'msg': msg})
    except Exception as e:
        msg = "Something Went Wrong Please contact with Administrator !"
        return render(request, 'login_attempt.html', {'msg': msg})
    return render(request, 'login_attempt.html', {'state': state, 'cat': cat})


def logout_attempt(request):
    logout(request)
    return redirect('login_attempt')


def register_attempt(request):
    state = State.objects.all()
    cat = VenuCategory.objects.all()[:1]
    try:
        if request.method == 'POST':
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            username = request.POST.get('username')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            password1 = request.POST.get('password1')
            password2 = request.POST.get('password2')
            if User.objects.filter(username=username).exists():
                msg = "username Already Exists!"
                return render(request, 'register_attempt.html', {'msg': msg})
            if User.objects.filter(email=email).exists():
                msg = "Email Address Already Exists!"
                return render(request, 'register_attempt.html', {'msg': msg})
            if User.objects.filter(phone=phone).exists():
                msg = "Phone Number Already Exists!"
                return render(request, 'register_attempt.html', {'msg': msg})
            if password1 != password2:
                msg = "Did Not Match Password!"
                return render(request, 'register_attempt.html', {'msg': msg})
            data = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email,
                                            is_customer=True,
                                            phone=phone)
            data.set_password(password2)
            data.save()
            var = Profile.objects.create(user=data, first_name=first_name, last_name=last_name, email=email,
                                         phone=phone)
            var.save()
            return redirect('login_attempt')
    except Exception as e:
        msg = "Something Went Wrong Please Contact with Administrator !"
        return render(request, 'register_attempt.html', {'msg': msg})

    return render(request, 'register_attempt.html', {'state': state, 'cat': cat})


def agent_register_attempt(request):
    state = State.objects.all()
    cat = VenuCategory.objects.all()[:1]
    try:
        if request.method == 'POST':
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            username = request.POST.get('username')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            password1 = request.POST.get('password1')
            password2 = request.POST.get('password2')
            if User.objects.filter(username=username).exists():
                msg = "username Already Exists!"
                return render(request, 'agent_register_attempt.html', {'msg': msg})
            if User.objects.filter(email=email).exists():
                msg = "Email Address Already Exists!"
                return render(request, 'agent_register_attempt.html', {'msg': msg})
            if User.objects.filter(phone=phone).exists():
                msg = "Phone Number Already Exists!"
                return render(request, 'agent_register_attempt.html', {'msg': msg})
            if password1 != password2:
                msg = "Did Not Match Password!"
                return render(request, 'agent_register_attempt.html', {'msg': msg})
            data = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email,
                                            is_agent=True,
                                            phone=phone)
            data.set_password(password2)
            data.save()
            var = Profile.objects.create(user=data, first_name=first_name, last_name=last_name, email=email,
                                         phone=phone)
            var.save()
            return redirect('login_attempt')
    except Exception as e:
        msg = "Something Went Wrong Please contact With Administrator !"
        return render(request, 'agent_register_attempt.html', {'msg': msg})
    return render(request, 'agent_register_attempt.html', {'state': state, 'cat': cat})


def change_pass(request):
    state = State.objects.all()
    cat = VenuCategory.objects.all()[:1]
    if not request.user.is_authenticated:
        return redirect('login_attempt')
    if request.method == 'POST':
        oldpass = request.POST.get('oldpass')
        newpass = request.POST.get('newpass')

        if oldpass == "" or newpass == "":
            msg = "All Field is Required"
            return render(request, 'forgetpassword.html', {'msg': msg})

        user = authenticate(username=request.user, password=oldpass)

        if user is not None:
            if len(newpass) < 8:
                msg = "Your Password at least minimum 8 character"
                return render(request, 'forgetpassword.html', {'msg': msg})

        user = User.objects.get(username=request.user)
        user.set_password(newpass)
        user.save()
        return redirect('logout_view')
    return render(request, 'forgetpassword.html', {'state': state, 'cat': cat})


def aboutus(request):
    state = State.objects.all()
    cat = VenuCategory.objects.all()[:1]
    return render(request, 'aboutus.html', {'state': state, 'cat': cat})


def blog_section(request):
    state = State.objects.all()
    cat = VenuCategory.objects.all()[:1]
    blg = Blog.objects.all()
    return render(request, 'blog_section.html', {'blg': blg, 'state': state, 'cat': cat})


def blog_details(request, slug):
    blg = Blog.objects.get(slug=slug)
    comment = BlogComment.objects.filter(blog=blg)
    blog = Blog.objects.all().order_by('-id')
    state = State.objects.all()
    cat = VenuCategory.objects.all()[:1]
    if request.method == 'POST':
        content = request.POST.get('message')
        user = request.user
        blog = blg
        data = BlogComment.objects.create(
            content=content, user=user, blog=blog)
        data.save()
        blg = Blog.objects.get(slug=slug)
        msg = 'Comment Created Successfully!'
        return render(request, 'blog_details.html', {'blg': blg, 'msg': msg, 'blog': blog})
    return render(request, 'blog_details.html',
                  {'blg': blg, 'comment': comment, 'state': state, 'cat': cat, 'blog': blog})


def statehotel(request, slug):
    state = State.objects.get(slug=slug)
    hotel = Venu.objects.filter(state=state)
    offer = OfferSlider.objects.all()
    p = Paginator(hotel, 10)
    page_number = request.GET.get('page')
    try:
        page_obj = p.get_page(page_number)
    except PageNotAnInteger:
        page_obj = p.page(1)
    except EmptyPage:
        page_obj = p.page(p.num_pages)
    state = State.objects.all()
    cat = VenuCategory.objects.all()[:1]
    return render(request, 'statehotel.html',
                  {'hotel': hotel, 'state': state, 'cat': cat, 'page_obj': page_obj, 'offer': offer})


def categoryhotel(request, slug):
    venu_cat = VenuCategory.objects.get(slug=slug)
    hotel = Hotel.objects.filter(cat=venu_cat)
    print(venu_cat.img, "===========================")
    offer = OfferSlider.objects.all()
    p = Paginator(hotel, 10)
    page_number = request.GET.get('page')
    try:
        page_obj = p.get_page(page_number)
    except PageNotAnInteger:
        page_obj = p.page(1)
    except EmptyPage:
        page_obj = p.page(p.num_pages)
    state = State.objects.all()
    cat = VenuCategory.objects.all()[:1]
    scat = VenuCategory.objects.all()
    return render(request, 'categoryhotel.html', {'hotel': hotel, 'state': state, 'cat': cat, "page_obj": page_obj,
                                                  'scat': scat, 'offer': offer, 'venu_cat': venu_cat})


def room_list(request, slug):
    # try:
    hotels = get_object_or_404(Hotel, slug=slug)
    hotel = Venu.objects.filter(hotel=hotels)
    offer = OfferSlider.objects.all()
    p = Paginator(hotel, 2)
    page_number = request.GET.get('page')
    try:
        page_obj = p.get_page(page_number)
    except PageNotAnInteger:
        page_obj = p.page(1)
    except EmptyPage:
        page_obj = p.page(p.num_pages)
    state = State.objects.all()
    cat = VenuCategory.objects.all()[:1]
    scat = VenuCategory.objects.all()
    # print(cat.name)
    return render(request, 'hotels_list.html', {'hotel': hotel, 'state': state, 'cat': cat, "page_obj": page_obj,
                                              'scat': scat, 'offer': offer, 'hotels': hotels})
    # except Exception as E:
    #     return HttpResponse("<h1>Hotel Image Not Found !</h1>")


def hotel_details(request, slug):
    ht = get_object_or_404(Venu, slug=slug)
    state = State.objects.all()
    cat = VenuCategory.objects.all()[:1]
    try:
        if request.method == 'POST':
            try:
                check_in = request.POST.get('check_in')
            except Exception as e:
                msg = "Please Input Check In Date !"
                return render(request, 'hotel_details.html', {"msg": msg})

            try:
                check_out = request.POST.get('check_out')
            except Exception as e:
                msg = "Please Input Check Out Date !"
                return render(request, 'hotel_details.html', {"msg": msg})

            guest = request.POST.get("guest")
            children = request.POST.get('children')
            room = request.POST.get('room')
            hotel_id = ht.id
            if request.user.is_authenticated:
                price = ht.total_budget
                user_type = "Is_Customer"
            if request.user.is_agent:
                price = ht.agent_price
                user_type = "Is_Agent"
            user_id = request.user.id
            hotel = Venu.objects.get(id=hotel_id)
            user = User.objects.get(id=user_id)
            reservation_id = random.randint(99999999, 999999999)
            data = Reservation.objects.create(check_in=check_in, check_out=check_out, guest=guest, children=children,
                                              room=room, hotel=hotel, user=user, mobile=request.user.phone,
                                              name=request.user.first_name + " " + request.user.last_name,
                                              email=request.user.email, reservation_id=reservation_id, price=price,
                                              user_type=user_type)
            data.save()
            return render(request, 'success.html', {'reservation_id': reservation_id})
    except Exception as e:
        return redirect('register_attempt')
    return render(request, 'hotel_details.html', {'ht': ht, 'state': state, 'cat': cat})


def searchfilter(request):
    blg = Blog.objects.all()
    cat = VenuCategory.objects.all()[:1]
    city = City.objects.all()
    state = State.objects.all()
    # location = Location.objects.all()
    related = Hotel.objects.all()
    # budget = AddBudget.objects.all()
    # facility = AddFacility.objects.all()
    # sm_cat = SimilarCategory.objects.all()
    slider = Slider.objects.all()
    venu = Venu.objects.all()
    hme = Venu.objects.all()[:3]
    #   hotel = Hotels.objects.all()[:3]
    context = {'cat': cat, 'city': city, 'related': related, 'venu': venu,
               'state': state, 'blg': blg, 'hme': hme, 'slider': slider}
    if request.method == 'POST':
        state = State.objects.all()
        hotel_id = request.POST.get('hotel')
        hotel = Hotel.objects.get(id=hotel_id)
        room = Venu.objects.filter(hotel=hotel)
        p = Paginator(room, 10)
        page_number = request.GET.get('page')
        try:
            page_obj = p.get_page(page_number)
        except PageNotAnInteger:
            page_obj = p.page(1)
        except EmptyPage:
            page_obj = p.page(p.num_pages)
        return render(request, 'search_hotels.html', {'page_obj': page_obj, 'hotels': hotel,'cat':cat, 'state': state})
    return render(request, 'home.html', context)


def search_filter(request):
    cat = VenuCategory.objects.all()[:1]
    state = State.objects.all()
    city = City.objects.all()
    # location = Location.objects.all()
    related = Hotel.objects.all()
    # budget = AddBudget.objects.all()
    # facility = AddFacility.objects.all()
    # sm_cat = SimilarCategory.objects.all()
    venu = Venu.objects.all()

    context = {'cat': cat, 'city': city, 'related': related, 'state': state, 'venu': venu}
    try:
        if request.method == 'POST':
            check_in = request.POST.get('check_in')
            check_out = request.POST.get('check_out')

            data = Venu.objects.filter(
                check_in__gte=check_in, check_out__lte=check_out)
            p = Paginator(data, 5)
            page_number = request.GET.get('page')
            try:
                page_obj = p.get_page(page_number)
            except PageNotAnInteger:
                page_obj = p.page(1)
            except EmptyPage:
                page_obj = p.page(p.num_pages)
            return render(request, 'search_hotels.html', {'page_obj': page_obj})
    except Exception as e:
        msg = "Something Went Wrong please input correct fields!"
        return render(request, 'home.html', {'msg': msg})
    return render(request, 'home.html', context)


def contactus(request):
    cat = VenuCategory.objects.all()[:1]
    state = State.objects.all()
    try:
        if request.method == 'POST':
            first_name = request.POST.get('fname')
            last_name = request.POST.get('lname')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            msg = request.POST.get('msg')

            data = ContactUs.objects.create(first_name=first_name, last_name=last_name, email=email, phone=phone,
                                            msg=msg)
            data.save()
            msg = "Your Contact Details Has Been Successfully Added!"
            return render(request, 'contactus.html', {'msg': msg})
    except Exception as e:
        msg = "Something Went Wrong Please After Sometimes later!"
        return render(request, 'contactus.html', {'msg': msg})
    return render(request, 'contactus.html', {'cat': cat, 'state': state})


def gallery(request):
    gi = GalleryImage.objects.all().order_by('-id')
    cat = VenuCategory.objects.all()[:1]
    city = City.objects.all()
    state = State.objects.all()
    # location = Location.objects.all()
    related = Hotel.objects.all()
    # budget = AddBudget.objects.all()
    # facility = AddFacility.objects.all()
    # sm_cat = SimilarCategory.objects.all()
    venu = Venu.objects.all()

    context = {'cat': cat, 'city': city, 'related': related, 'state': state, 'venu': venu, 'gi': gi}
    return render(request, 'gallery.html', context)


def testing(request, slug):
    cat = Hotel.objects.get(slug=slug)
    hotel = Venu.objects.filter(hotel=cat)
    p = Paginator(hotel, 10)
    page_number = request.GET.get('page')
    try:
        page_obj = p.get_page(page_number)
    except PageNotAnInteger:
        page_obj = p.page(1)
    except EmptyPage:
        page_obj = p.page(p.num_pages)
    state = State.objects.all()
    cat = VenuCategory.objects.all()[:1]
    scat = VenuCategory.objects.all()
    return render(request, 'test.html', {'hotel': hotel, 'state': state, 'cat': cat, "page_obj": page_obj,
                                         'scat': scat})


class HotelFilter(django_filters.FilterSet):
    state__name = django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = Hotel
        fields = ['state']


class HotelsAPIView(ListAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializers
    filter_backends = [DjangoFilterBackend]
    filterset_class = HotelFilter


def career(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        mobile = request.POST.get('mobile')
        position = request.POST.get('position')
        email = request.POST.get('email')
        msg = request.POST.get('msg')
        cv = request.FILES['cv']
        data = Career.objects.create(
            fname=fname, mobile=mobile, position=position, email=email, cv=cv, msg=msg)
        data.save()
        msg = "Your Details Has Been Successfully Sent !"
        return render(request, 'career.html', {'msg': msg})

    return render(request, 'career.html')


def bookevent(request):
    state = State.objects.all()
    cat = VenuCategory.objects.all()[:1]
    event = EventText.objects.all()[:1]
    sl = EventSlider.objects.all()
    try:
        if request.method == 'POST':
            bride_groom = request.POST.get('bride_groom')
            function = request.POST.get('function')
            date = request.POST.get('date')
            time = request.POST.get('time')
            number_of_room = request.POST.get('number_of_room')
            location = request.POST.get('location')
            guest_capacity = request.POST.get('guest_capacity')
            number_of_night = request.POST.get('number_of_night')
            contact_number = request.POST.get('contact_number')
            email_address = request.POST.get('email_address')
            msg = request.POST.get('msg')
            data = MarriageEvents.objects.create(bride_groom=bride_groom, function=function, date=date, time=time,
                                                 number_of_room=number_of_room, location=location,
                                                 guest_capacity=guest_capacity,
                                                 number_of_night=number_of_night, contact_number=contact_number,
                                                 email_address=email_address,
                                                 msg=msg)
            data.save()
            msg = "Your Details Has Been Successfully sent!"
            return render(request, 'bookevent.html', {'msg': msg})
    except Exception as E:
        return render(request, 'bookevent.html', {'msg': "Please Input Correct Date and Time"})
    return render(request, 'bookevent.html', {'state': state, 'event': event, 'sl': sl, 'cat':cat})


def partner(request):
    state = State.objects.all()
    cat = VenuCategory.objects.all()[:1]

    if request.method == 'POST':
        fname = request.POST.get('fname')
        hotel_name = request.POST.get('hotel_name')
        mobile = request.POST.get('mobile')
        address = request.POST.get('address')
        email = request.POST.get('email')
        room = request.POST.get('room')
        msg = request.POST.get('msg')

        data = Partner.objects.create(fname=fname, hotel_name=hotel_name,
                                      mobile=mobile, address=address, email=email, room=room, msg=msg)
        data.save()
        msg = "Your Details Has Been Sent Successfully !"
        return render(request, 'partner.html', {'msg': msg})

    return render(request, 'partner.html', {'state': state, 'cat':cat})
