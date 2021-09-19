from django.urls import path
from .views import registeruser,homeview,loginuser,logoutuser,change_password
from django.contrib.auth.views import PasswordResetView,PasswordResetDoneView,PasswordResetConfirmView,PasswordResetCompleteView


urlpatterns=[
    path('home/',homeview,name='home'),
    path('register/',registeruser,name='register'),
    path('login/',loginuser,name='login'),
    path('logout/',logoutuser,name='logout'),
    path('change_password/',change_password,name='change_password'),

    path('reset_password/',PasswordResetView.as_view(template_name = "testapp/reset_password.html"), name ='reset_password'),
    path('reset_password_sent/',PasswordResetDoneView.as_view(template_name = "testapp/password_reset_sent.html"), name ='password_reset_done'),
    path('reset/<uidb64>/<token>',PasswordResetConfirmView.as_view(template_name = "testapp/password_reset_form.html"), name ='password_reset_confirm'),
    path('reset_password_complete/',PasswordResetCompleteView.as_view(template_name = "testapp/password_reset_done.html"), name ='password_reset_complete'),

    

]