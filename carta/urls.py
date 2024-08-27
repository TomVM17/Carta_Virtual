from django.urls import path
from . import views

urlpatterns = [
    path("", views.inicio, name="home"),
    path("menu/", views.menu, name="menu"),
    path("localizacion/", views.localizaciones, name="localizacion")
]
