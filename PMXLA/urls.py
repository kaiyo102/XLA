from . import views 
from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.loginpage, name='loginpage'),
    path('logout/', auth_views.LogoutView.as_view() , name='logout'),

]