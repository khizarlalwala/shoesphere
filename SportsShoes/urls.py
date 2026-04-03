from django.urls import path
from SportsShoes import views
from . import views

urlpatterns = [
    path("",views.home, name="home"),
    path("nike/",views.nike, name="nike"),
    path("adidas/",views.adidas, name="adidas"),
    path("asics/",views.asics, name="asics"),
    path("puma/",views.puma, name="puma"),
    path("comet/",views.comet, name="comet"),
    
    path('',views.collection,name='collection'),

    path('add/',views.add_shoe,name='add_shoe'),

    path('update/<int:id>/',views.update_shoe,name='update_shoe'),

    path('delete/<int:id>/',views.delete_shoe,name='delete_shoe'),

    ]