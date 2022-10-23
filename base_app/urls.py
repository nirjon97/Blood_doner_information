from django.contrib import admin
from django.urls import path,include
from .views import login_register_option


urlpatterns = [
    path('' ,login_register_option, name='login_register_option'),
    path('information/', include('blood_doner_information_app.urls')),
    path('authentication/', include('authentication_app.urls')),
]