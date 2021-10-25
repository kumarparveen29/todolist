from django.contrib import admin
from django.urls import path, include
from index import views

urlpatterns = [
    path('', views.home, name="home"),
    path('home', views.home, name="home"),
    path('list/<str:title>', views.list, name="list"),
    path('login', views.loginuser, name="login"),
    path('signup', views.signupuser, name="signup"),
    path('logout', views.logoutuser, name="logout"),
    path('delete/<str:task>/<str:name>', views.delete, name="delete"),
    path('del/<str:lst>', views.close, name="close"),
    path('contact', views.contact, name="contact"),
    path('about', views.about, name="about")
]