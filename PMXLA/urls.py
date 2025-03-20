from . import views 
from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.mainpage, name='mainpage'),
    path('loginpage/', views.loginpage, name='loginpage'),
    path('logout/', auth_views.LogoutView.as_view() , name='logout'),
    path('loginXLA/', views.loginXLA, name='loginXLA'),
    path('signuppage/', views.signuppage, name='signuppage'),
    path('signup/', views.signup, name='signup'),
    path('homepage/', views.homepage, name='homepage'),
    path('userpage/', views.userpage, name='userpage'),
    path('mainpage/', views.mainpage, name='mainpage'),
    path('xylyanhpage/', views.xylyanhpage, name='xylyanhpage'),


]