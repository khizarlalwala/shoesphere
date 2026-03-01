from django.urls import path
from SportsShoes import views

urlpatterns =[
    path("",views.home, name="home"),
    path("nike/",views.nike, name="nike"),
    path("adidas/",views.adidas, name="adidas"),
    path("asics/",views.asics, name="asics"),
    path("puma/",views.puma, name="puma"),
]