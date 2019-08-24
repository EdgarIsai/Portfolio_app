from django.urls import path

from . import views

urlpatterns = [
    path("", views.home),
    path("menu/", views.menu),
    path("discount/", views.discount),
    path("contact/", views.contact),
]
