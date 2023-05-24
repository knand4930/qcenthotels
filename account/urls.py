from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('login/attempt', login_attempt, name='login_attempt'),
    path('logout/attempt', logout_attempt, name='logout_attempt'),
    path('register/attempt', register_attempt, name='register_attempt'),
    path('change/password', change_pass, name='change_pass'),
    path('blog/section', blog_section, name='blog_section'),
    path('blog/details/<slug:slug>/', blog_details, name='blog_details'),
    path('state/hotel/<slug:slug>/', statehotel, name='statehotel'),
    path('category/hotel/<slug:slug>/', categoryhotel, name='categoryhotel'),
    path('room/list/<slug:slug>/', room_list, name='room_list'),
    path('hotel/details/<slug:slug>/', hotel_details, name='hotel_details'),

    path('search/filter', searchfilter, name='searchfilter'),
    path('search/filters', search_filter, name='search_filter'),

    path('contact/us', contactus, name='contactus'),
    path('agent/register/attempt', agent_register_attempt, name='agent_register_attempt'),
    path('about/us', aboutus, name='aboutus'),
    path('gallery', gallery, name='gallery'),
    path('testing/<slug>', testing, name='testing'),
    path('get-hotel/', HotelsAPIView.as_view(), name="hotel_api_view"),
    path('career', career, name="career"),
    path('bookevent', bookevent, name='bookevent'),
    path('partner', partner, name='partner'),
]   
