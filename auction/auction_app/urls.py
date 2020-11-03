from django.urls import path
from .views import *

urlpatterns = [
    path('index', index),
    path('contact', contact),
    path('register', RegistrationApi.as_view()),
    path('login', LoginApi.as_view()),
    path('vendor', vendor_page),
    path('bidder', bidder_page),

]