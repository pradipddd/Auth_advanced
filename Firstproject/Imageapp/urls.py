from django.urls import path
from .views import Simple_upload,model_form_upload,show_upload_view

urlpatterns=[
    path('simple_upload/',Simple_upload,name='simple_upload'),
    path('model_form_upload/',model_form_upload,name='model_form_upload'),
    path('show_upload/',show_upload_view,name='show_upload'),

]