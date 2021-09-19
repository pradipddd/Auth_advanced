from django.urls import path
from .views import Laptop_add_view, Laptop_show_view

urlpatterns=[
    path('laptop_add/',Laptop_add_view,name='laptop_add'),
    path('laptop_show/',Laptop_show_view,name='laptop_show'),
]