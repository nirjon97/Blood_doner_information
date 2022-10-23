from django.urls import path
from .views import Home,search_data_from_api,create_doner,your_data_details,all_data_details,your_data_json_view,your_data_template_view,all_data_template_view,all_data_json_view
from rest_framework import generics

urlpatterns = [
    path('home/', Home, name='Home'),
    path('your_data_details/',your_data_details,name='your_data_details'),
    path('all_data_details/',all_data_details,name='all_data_details'),
    path('json_view/',your_data_json_view,name='your_data_json_view'),
    path('template_view/',your_data_template_view,name='your_data_template_view'),
    path('json_view_all/',all_data_json_view,name='all_data_json_view'),
    path('template_view_all/',all_data_template_view,name='all_data_template_view'),
    path('create/',create_doner,name='create_doner'),
#    path('get_data_api/',get_data_from_api,name='get_data_from_api'),
    path('search/',search_data_from_api.as_view(),name='search_data_from_api')




]