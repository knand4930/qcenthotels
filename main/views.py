from django.core.paginator import PageNotAnInteger, Paginator, EmptyPage
from django.shortcuts import render, redirect
from .models import *


# Create your views here.


def adminpanel(request):
    if not request.user.is_superuser:
        return redirect('login_attempt')
    total_hotel = Venu.objects.all().count()
    total_booking = Reservation.objects.all().count()
    total_blog = Blog.objects.all().count()
    return render(request, 'adminpanel.html', {'total_hotel': total_hotel, 'total_booking': total_booking,
                                               'total_blog': total_blog})


def alllead(request):
    if not request.user.is_superuser:
        return redirect('login_attempt')
    var = Reservation.objects.all()
    p = Paginator(var, 5)
    page_number = request.GET.get('page')
    try:
        page_obj = p.get_page(page_number)
    except PageNotAnInteger:
        page_obj = p.page(1)
    except EmptyPage:
        page_obj = p.page(p.num_pages)
    context = {'page_obj': page_obj}
    return render(request, 'alllead.html', context)


def slidersection(request):
    if not request.user.is_superuser:
        return redirect('login_attempt')
    if request.method == 'POST':
        title = request.POST.get('title')
        img = request.FILES['img']
        if Slider.objects.filter(title=title).exists():
            msg = "TTitle Already Exists !"
            return render(request, 'slidersection.html', {'msg': msg})
        data = Slider.objects.create(title=title, img=img)
        data.save()
    var = Slider.objects.all()
    p = Paginator(var, 5)
    page_number = request.GET.get('page')
    try:
        page_obj = p.get_page(page_number)
    except PageNotAnInteger:
        page_obj = p.page(1)
    except EmptyPage:
        page_obj = p.page(p.num_pages)
    context = {'page_obj': page_obj}
    return render(request, 'slidersection.html', context)


def offerslider(request):
    if not request.user.is_superuser:
        return redirect('login_attempt')
    if request.method == 'POST':
        title = request.POST.get('title')
        img = request.FILES['img']
        if OfferSlider.objects.filter(title=title).exists():
            msg = "Title Already Exists !"
            return render(request, 'offerslider.html', {'msg': msg})
        data = OfferSlider.objects.create(title=title, img=img)
        data.save()
    var = OfferSlider.objects.all()
    p = Paginator(var, 5)
    page_number = request.GET.get('page')
    try:
        page_obj = p.get_page(page_number)
    except PageNotAnInteger:
        page_obj = p.page(1)
    except EmptyPage:
        page_obj = p.page(p.num_pages)
    context = {'page_obj': page_obj}
    return render(request, 'offerslider.html', context)


# def addmenu(request):
#     if not request.user.is_superuser:
#         return redirect('login_attempt')
#     if request.method == 'POST':
#         title = request.POST.get('title')
#         if Menu.objects.filter(title=title).exists():
#             msg = "Menu Already Exists !"
#             return render(request, 'addmenu.html', {'msg': msg})
#         data = Menu.objects.create(title=title)
#         data.save()
#     var = Menu.objects.all()
#     p = Paginator(var, 5)
#     page_number = request.GET.get('page')
#     try:
#         page_obj = p.get_page(page_number)
#     except PageNotAnInteger:
#         page_obj = p.page(1)
#     except EmptyPage:
#         page_obj = p.page(p.num_pages)
#     context = {'page_obj': page_obj}
#     return render(request, 'addmenu.html', context)


# def addubmenu(request):
#     if not request.user.is_superuser:
#         return redirect('login_attempt')
#     val = Menu.objects.all()
#     if request.method == 'POST':
#         title = request.POST.get('title')
#         menu_id = request.POST.get('menu')
#         menu = Menu.objects.get(id=menu_id)
#         if SubMenu.objects.filter(title=title).exists():
#             msg = "Sub Menu Already Exists !"
#             return render(request, 'addubmenu.html', {'msg': msg})
#         data = SubMenu.objects.create(title=title, menu=menu)
#         data.save()
#     var = SubMenu.objects.all()
#     p = Paginator(var, 5)
#     page_number = request.GET.get('page')
#     try:
#         page_obj = p.get_page(page_number)
#     except PageNotAnInteger:
#         page_obj = p.page(1)
#     except EmptyPage:
#         page_obj = p.page(p.num_pages)
#     context = {'page_obj': page_obj, 'val': val}
#     return render(request, 'addubmenu.html', context)


# def aboutcategory(request):
#     if not request.user.is_superuser:
#         return redirect('login_attempt')
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         txt = request.POST.get('txt')
#         icon = request.FILES['icon']
#         if AboutCategory.objects.filter(name=name).exists():
#             msg = "About Category Already Exists !"
#             return render(request, 'aboutcategory.html', {'msg': msg})
#         data = AboutCategory.objects.create(name=name, txt=txt, icon=icon)
#         data.save()
#     var = AboutCategory.objects.all()
#     p = Paginator(var, 5)
#     page_number = request.GET.get('page')
#     try:
#         page_obj = p.get_page(page_number)
#     except PageNotAnInteger:
#         page_obj = p.page(1)
#     except EmptyPage:
#         page_obj = p.page(p.num_pages)
#     context = {'page_obj': page_obj}
#     return render(request, 'aboutcategory.html', context)


# def eventcategory(request):
#     if not request.user.is_superuser:
#         return redirect('login_attempt')
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         txt = request.POST.get('txt')
#         icon = request.FILES['icon']
#         img = request.FILES['img']
#         if EventCategory.objects.filter(name=name).exists():
#             msg = "Event Category Already Exists!"
#             return render(request, 'eventcategory.html', {'msg': msg})
#         data = EventCategory.objects.create(name=name, txt=txt, icon=icon, img=img)
#         data.save()
#     var = EventCategory.objects.all()
#     p = Paginator(var, 5)
#     page_number = request.GET.get('page')
#     try:
#         page_obj = p.get_page(page_number)
#     except PageNotAnInteger:
#         page_obj = p.page(1)
#     except EmptyPage:
#         page_obj = p.page(p.num_pages)
#     context = {'page_obj': page_obj}
#     return render(request, 'eventcategory.html', context)


def blogcategory(request):
    if not request.user.is_superuser:
        return redirect('login_attempt')
    if request.method == 'POST':
        name = request.POST.get('name')
        # txt = request.POST.get('txt')
        img = request.FILES['img']
        if BlogCategory.objects.filter(name=name).exists():
            msg = 'Blog category Already Exists!'
            return render(request, 'blogcategory.html', {'msg': msg})
        data = BlogCategory.objects.create(name=name, img=img)
        data.save()
    var = BlogCategory.objects.all()
    p = Paginator(var, 5)
    page_number = request.GET.get('page')
    try:
        page_obj = p.get_page(page_number)
    except PageNotAnInteger:
        page_obj = p.page(1)
    except EmptyPage:
        page_obj = p.page(p.num_pages)
    context = {'page_obj': page_obj}
    return render(request, 'blogcategory.html', context)


def venusecatrgory(request):
    if not request.user.is_superuser:
        return redirect('login_attempt')
    return render(request, 'venusecatrgory.html')


def gallerycategory(request):
    if not request.user.is_superuser:
        return redirect('login_attempt')
    if request.method == 'POST':
        name = request.POST.get('name')
        img = request.FILES['img']
        if GalleryCategory.objects.filter(name=name).exists():
            msg = "Gallery Category Already Exists !"
            return render(request, 'gallerycategory.html', {'msg': msg})
        data = GalleryCategory.objects.create(name=name, img=img)
        data.save()
    var = GalleryCategory.objects.all()
    p = Paginator(var, 5)
    page_number = request.GET.get('page')
    try:
        page_obj = p.get_page(page_number)
    except PageNotAnInteger:
        page_obj = p.page(1)
    except EmptyPage:
        page_obj = p.page(p.num_pages)
    context = {'page_obj': page_obj}
    return render(request, 'gallerycategory.html', context)


def gallerylist(request):
    if not request.user.is_superuser:
        return redirect('login_attempt')
    gc = GalleryCategory.objects.all()
    if request.method == 'POST':
        cat_id = request.POST.get('cat')
        title = request.POST.get('title')
        img = request.FILES['img']
        if GalleryImage.objects.filter(title=title).exists():
            msg = "Title Already Exists !"
            return render(request, 'gallerylist.html', {'msg': msg})
        cat = GalleryCategory.objects.get(id=cat_id)
        data = GalleryImage.objects.create(cat=cat, title=title, img=img)
        data.save()
    var = GalleryImage.objects.all()
    p = Paginator(var, 5)
    page_number = request.GET.get('page')
    try:
        page_obj = p.get_page(page_number)
    except PageNotAnInteger:
        page_obj = p.page(1)
    except EmptyPage:
        page_obj = p.page(p.num_pages)
    context = {'page_obj': page_obj, 'gc': gc}
    return render(request, 'gallerylist.html', context)


def videoist(request):
    if not request.user.is_superuser:
        return redirect('login_attempt')
    gc = GalleryCategory.objects.all()
    if request.method == 'POST':
        cat_id = request.POST.get('cat')
        title = request.POST.get('title')
        lnk = request.POST.get('lnk', None)
        # file = request.FILES['file', None]
        if GalleryVideo.objects.filter(title=title).exists():
            msg = "Title Already Exists !"
            return render(request, 'videoist.html', {'msg': msg})
        cat = GalleryCategory.objects.get(id=cat_id)
        data = GalleryVideo.objects.create(cat=cat, title=title, lnk=lnk)
        data.save()
    var = GalleryVideo.objects.all()
    p = Paginator(var, 5)
    page_number = request.GET.get('page')
    try:
        page_obj = p.get_page(page_number)
    except PageNotAnInteger:
        page_obj = p.page(1)
    except EmptyPage:
        page_obj = p.page(p.num_pages)
    context = {'page_obj': page_obj, 'gc': gc}
    return render(request, 'videoist.html', context)


def addblog(request):
    if not request.user.is_superuser:
        return redirect('login_attempt')
    abm = BlogCategory.objects.all()
    if request.method == 'POST':
        cat_id = request.POST.get('cat')
        title = request.POST.get('title')
        caption = request.POST.get('caption')
        meta_title = request.POST.get('meta_title')
        meta_keyword = request.POST.get('meta_keyword')
        meta_description = request.POST.get('meta_description')
        img = request.FILES['img']
        txt = request.POST.get('txt', None)
        if Blog.objects.filter(title=title).exists():
            msg = "Title Already Exists !"
            return render(request, 'addblog.html', {'msg': msg})
        cat = BlogCategory.objects.get(id=cat_id)
        data = Blog.objects.create(cat=cat, title=title, caption=caption, meta_title=meta_title,
                                   meta_keyword=meta_keyword, meta_description=meta_description, img=img, txt=txt)
        data.save()
        msg = "Your Blog Has Been Added Successfully"
        return render(request, 'addblog.html', {'msg': msg})
    return render(request, 'addblog.html', {'abm': abm})


def viewblog(request):
    if not request.user.is_superuser:
        return redirect('login_attempt')
    var = Blog.objects.all()
    p = Paginator(var, 5)
    page_number = request.GET.get('page')
    try:
        page_obj = p.get_page(page_number)
    except PageNotAnInteger:
        page_obj = p.page(1)
    except EmptyPage:
        page_obj = p.page(p.num_pages)
    context = {'page_obj': page_obj}
    return render(request, 'viewblog.html', context)


# def addevents(request):
#     if not request.user.is_superuser:
#         return redirect('login_attempt')
#     ce = EventCategory.objects.all()
#     if request.method == 'POST':
#         cat_id = request.POST.get('cat')
#         title = request.POST.get('title')
#         caption = request.POST.get('caption')
#         img = request.FILES['img']
#         txt = request.POST.get('txt')
#         if Event.objects.filter(title=title).exists():
#             msg = "Title Already Exists !"
#             return render(request, 'addevents.html', {'msg': msg})
#         cat = EventCategory.objects.get(id=cat_id)
#         data = Event.objects.create(cat=cat, title=title, caption=caption, img=img, txt=txt)
#         data.save()
#         msg = "Event Has Been Successfully Added !"
#         return render(request, 'addevents.html', {'msg': msg})
#     return render(request, 'addevents.html', {'ce': ce})


# def viewevents(request):
#     if not request.user.is_superuser:
#         return redirect('login_attempt')
#     var = Event.objects.all()
#     p = Paginator(var, 5)
#     page_number = request.GET.get('page')
#     try:
#         page_obj = p.get_page(page_number)
#     except PageNotAnInteger:
#         page_obj = p.page(1)
#     except EmptyPage:
#         page_obj = p.page(p.num_pages)
#     context = {'page_obj': page_obj}
#     return render(request, 'viewevents.html', context)


# def addtestimonials(request):
#     if not request.user.is_superuser:
#         return redirect('login_attempt')
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         postion = request.POST.get('postion')
#         img = request.FILES['img']
#         txt = request.POST.get('txt')
#         if Testimonial.objects.filter(name=name).exists():
#             msg = "Name Already Exists !"
#             return render(request, 'addtestimonials.html', {'msg': msg})
#         data = Testimonial.objects.create(name=name, postion=postion, img=img, txt=txt)
#         data.save()
#     var = Testimonial.objects.all()
#     p = Paginator(var, 5)
#     page_number = request.GET.get('page')
#     try:
#         page_obj = p.get_page(page_number)
#     except PageNotAnInteger:
#         page_obj = p.page(1)
#     except EmptyPage:
#         page_obj = p.page(p.num_pages)
#     context = {'page_obj': page_obj}
#     return render(request, 'addtestimonials.html', context)


def venucategory(request):
    if not request.user.is_superuser:
        return redirect('login_attempt')
    if request.method == 'POST':
        name = request.POST.get('name')
        if VenuCategory.objects.filter(name=name).exists():
            msg = "Venue Category Already Exists"
            return render(request, 'venucategory.html', {'msg': msg})
        data = VenuCategory.objects.create(name=name)
        data.save()
    var = VenuCategory.objects.all()
    p = Paginator(var, 5)
    page_number = request.GET.get('page')
    try:
        page_obj = p.get_page(page_number)
    except PageNotAnInteger:
        page_obj = p.page(1)
    except EmptyPage:
        page_obj = p.page(p.num_pages)
    context = {'page_obj': page_obj}

    return render(request, 'venucategory.html', context)


def addstate(request):
    if not request.user.is_superuser:
        return redirect('login_attempt')
    if request.method == 'POST':
        name = request.POST.get('name')
        if State.objects.filter(name=name).exists():
            msg = "State Already Exists"
            return render(request, 'addstate.html', {'msg': msg})
        data = State.objects.create(name=name)
        data.save()
    var = State.objects.all()
    p = Paginator(var, 5)
    page_number = request.GET.get('page')
    try:
        page_obj = p.get_page(page_number)
    except PageNotAnInteger:
        page_obj = p.page(1)
    except EmptyPage:
        page_obj = p.page(p.num_pages)
    context = {'page_obj': page_obj}

    return render(request, 'addstate.html', context)


def addcity(request):
    if not request.user.is_superuser:
        return redirect('login_attempt')
    if request.method == 'POST':
        name = request.POST.get('name')
        if City.objects.filter(name=name).exists():
            msg = "City Already Exists"
            return render(request, 'addcity.html', {'msg': msg})
        data = City.objects.create(name=name)
        data.save()
    var = City.objects.all()
    p = Paginator(var, 5)
    page_number = request.GET.get('page')
    try:
        page_obj = p.get_page(page_number)
    except PageNotAnInteger:
        page_obj = p.page(1)
    except EmptyPage:
        page_obj = p.page(p.num_pages)
    context = {'page_obj': page_obj}

    return render(request, 'addcity.html', context)


def addlocation(request):
    if not request.user.is_superuser:
        return redirect('login_attempt')
    if request.method == 'POST':
        name = request.POST.get('name')
        if Location.objects.filter(name=name).exists():
            msg = "Location Already Exists"
            return render(request, 'venucategory.html', {'msg': msg})
        data = Location.objects.create(name=name)
        data.save()
    var = Location.objects.all()
    p = Paginator(var, 5)
    page_number = request.GET.get('page')
    try:
        page_obj = p.get_page(page_number)
    except PageNotAnInteger:
        page_obj = p.page(1)
    except EmptyPage:
        page_obj = p.page(p.num_pages)
    context = {'page_obj': page_obj}

    return render(request, 'addlocation.html', context)


def hotel(request):
    if not request.user.is_superuser:
        return redirect('login_attempt')

    if request.method == 'POST':
        state_id = request.POST.get('state')
        name = request.POST.get('name')
        img = request.FILES['img']
        summary = request.POST.get('summary')
        state = State.objects.get(id=state_id)
        if Hotel.objects.filter(name=name).exists():
            msg = "Hotel Already Exists"
            return render(request, 'hotels_list.html', {'msg': msg})
        data = Hotel.objects.create(state=state, name=name, img=img, summary=summary)
        data.save()
    var = Hotel.objects.all()
    p = Paginator(var, 5)
    page_number = request.GET.get('page')
    try:
        page_obj = p.get_page(page_number)
    except PageNotAnInteger:
        page_obj = p.page(1)
    except EmptyPage:
        page_obj = p.page(p.num_pages)
    state = State.objects.all()
    return render(request, 'hotels_list.html', {'page_obj': page_obj, 'state': state})


# def add_budget(request):
#     if not request.user.is_superuser:
#         return redirect('login_attempt')
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         if AddBudget.objects.filter(name=name).exists():
#             msg = "Budget Already Exists"
#             return render(request, 'add_budget.html', {'msg': msg})
#         data = AddBudget.objects.create(name=name)
#         data.save()
#     var = AddBudget.objects.all()
#     p = Paginator(var, 5)
#     page_number = request.GET.get('page')
#     try:
#         page_obj = p.get_page(page_number)
#     except PageNotAnInteger:
#         page_obj = p.page(1)
#     except EmptyPage:
#         page_obj = p.page(p.num_pages)
#     context = {'page_obj': page_obj}
#     return render(request, 'add_budget.html', context)


# def add_facility(request):
#     if not request.user.is_superuser:
#         return redirect('login_attempt')
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         if AddFacility.objects.filter(name=name).exists():
#             msg = "Facility Already Exists"
#             return render(request, 'add_facility.html', {'msg': msg})
#         data = AddFacility.objects.create(name=name)
#         data.save()
#     var = AddFacility.objects.all()
#     p = Paginator(var, 5)
#     page_number = request.GET.get('page')
#     try:
#         page_obj = p.get_page(page_number)
#     except PageNotAnInteger:
#         page_obj = p.page(1)
#     except EmptyPage:
#         page_obj = p.page(p.num_pages)
#     context = {'page_obj': page_obj}
#     return render(request, 'add_facility.html', context)


# def similar_category(request):
#     if not request.user.is_superuser:
#         return redirect('login_attempt')
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         if SimilarCategory.objects.filter(name=name).exists():
#             msg = "Similar Category Already Exists"
#             return render(request, 'similar_category.html', {'msg': msg})
#         data = SimilarCategory.objects.create(name=name)
#         data.save()
#     var = SimilarCategory.objects.all()
#     p = Paginator(var, 5)
#     page_number = request.GET.get('page')
#     try:
#         page_obj = p.get_page(page_number)
#     except PageNotAnInteger:
#         page_obj = p.page(1)
#     except EmptyPage:
#         page_obj = p.page(p.num_pages)
#     context = {'page_obj': page_obj}
#     return render(request, 'similar_category.html', context)


def addvenueslisting(request):
    if not request.user.is_superuser:
        return redirect('login_attempt')
    cat = VenuCategory.objects.all()
    city = City.objects.all()
    state = State.objects.all()
    # location = Location.objects.all()
    hotel = Hotel.objects.all()
    # budget = AddBudget.objects.all()
    # facility = AddFacility.objects.all()
    gallery = GalleryCategory.objects.all()

    context = {'cat': cat, 'city': city, 'hotel': hotel,
               'sm_cat': gallery, 'state': state}
    if request.method == 'POST':
        cat_id = request.POST.get('cat')
        state_id = request.POST.get('state')
        city_id = request.POST.get('city')
        related_location_id = request.POST.get('related_location')

        budget = request.POST.get('budget')
        price_increase = request.POST.get('price_increase')
        agent = request.POST.get('agent')

        total_budget = (int(budget) * int(price_increase) / 100) + int(budget)

        agent_price = total_budget - (total_budget * int(agent) / 100)

        cat = VenuCategory.objects.get(id=cat_id)
        state = State.objects.get(id=state_id)
        city = City.objects.get(id=city_id)
        hotel = Hotel.objects.get(id=related_location_id)

        name = request.POST.get('name')
        parking = request.POST.get('parking')
        wifi = request.POST.get('wifi')
        breakfast = request.POST.get('breakfast')
        pool = request.POST.get('pool')
        reception = request.POST.get('reception')
        gym = request.POST.get('gym')

        img = request.FILES['img']

        summary = request.POST.get('summary')
        check_in = request.POST.get('check_in')
        check_out = request.POST.get('check_out')

        advance = request.POST.get('advance')
        cancelecation_charge = request.POST.get('cancelecation_charge')
#        if Venu.objects.filter(name=name).exists():
 #           msg = "Hotel Name Already Exists!"
  #          return render(request, 'addvenueslisting.html', {'msg': msg})

        data = Venu.objects.create(cat=cat, state=state, city=city, img=img, parking=parking, wifi=wifi, breakfast=breakfast,
                                   pool=pool, reception=reception, gym=gym,
                                   hotel=hotel, check_in=check_in, check_out=check_out,
                                   budget=budget, name=name, advance=advance, cancelecation_charge=cancelecation_charge,
                                   summary=summary, price_increase=price_increase,
                                   total_budget=total_budget, agent_price=agent_price, agent=agent)
        data.save()
        msg = "Your data Has Been Successfully Added!"
        return render(request, 'addvenueslisting.html', {'msg': msg})
    return render(request, 'addvenueslisting.html', context)


def viewvenueslisting(request):
    if not request.user.is_superuser:
        return redirect('login_attempt')
    var = Venu.objects.all()
    p = Paginator(var, 5)
    page_number = request.GET.get('page')
    try:
        page_obj = p.get_page(page_number)
    except PageNotAnInteger:
        page_obj = p.page(1)
    except EmptyPage:
        page_obj = p.page(p.num_pages)
    context = {'page_obj': page_obj}
    return render(request, 'viewvenueslisting.html', context)


def addvenuimages(request):
    if not request.user.is_superuser:
        return redirect('login_attempt')
    gc = Venu.objects.all()
    if request.method == 'POST':
        cat_id = request.POST.get('cat')
        title = request.POST.get('title')
        img = request.FILES['img']
        cat = Venu.objects.get(id=cat_id)
        data = VenuImages.objects.create(venu=cat, name=title, img=img)
        data.save()
    var = VenuImages.objects.all()
    p = Paginator(var, 5)
    page_number = request.GET.get('page')
    try:
        page_obj = p.get_page(page_number)
    except PageNotAnInteger:
        page_obj = p.page(1)
    except EmptyPage:
        page_obj = p.page(p.num_pages)
    context = {'page_obj': page_obj, 'gc': gc}
    return render(request, 'addvenuimages.html', context)
