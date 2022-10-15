from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("", views.index, name='home'),
    path("active", views.active),
    path("about", views.about),
    path("contact", views.contact),
    path("signup", views.signup),


]