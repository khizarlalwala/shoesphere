from django.urls import path
from SportsShoes import views

urlpatterns =[
    path("",views.home, name="home")
]