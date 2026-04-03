from django.shortcuts import render, redirect, get_object_or_404
from .models import Shoe
from .forms import ShoeForm
from django.http import JsonResponse





# COLLECTION PAGE
def collection(request):

    shoes = Shoe.objects.all()

    return render(request,'collection.html',{'shoes':shoes})


# CREATE SHOE
def add_shoe(request):

    if request.method == "POST":

        name = request.POST.get("name")
        price = request.POST.get("price")
        image = request.POST.get("image")

        shoe = Shoe.objects.create(
            name=name,
            price=price,
            image=image
        )

        return JsonResponse({
            "id": shoe.id,
            "name": shoe.name,
            "price": shoe.price,
            "image": shoe.image
        })

    shoes = Shoe.objects.all()

    return render(request,"add_shoe.html",{"shoes":shoes})


# UPDATE SHOE
def update_shoe(request,id):

    shoe = get_object_or_404(Shoe,id=id)

    if request.method == "POST":

        form = ShoeForm(request.POST,instance=shoe)

        if form.is_valid():
            form.save()
            return redirect('asics')

    else:
        form = ShoeForm(instance=shoe)

    shoes = Shoe.objects.all()

    return render(request,'add_shoe.html',{'form':form,'shoes':shoes})


# DELETE SHOE
def delete_shoe(request,id):

    shoe = get_object_or_404(Shoe,id=id)
    shoe.delete()

    return redirect('asics')


# WEBSITE PAGES

def home(request):
    return render(request, 'SportsShoes/home.html')

def puma(request):
    return render(request, 'SportsShoes/puma.html')

def adidas(request):
    return render(request, 'SportsShoes/adidas.html')

def nike(request):
    return render(request, 'SportsShoes/nike.html')

def comet(request):
    return render(request, 'SportsShoes/comet.html')


# ASICS PAGE (IMPORTANT FIX)
def asics(request):

    shoes = Shoe.objects.all()

    return render(request, 'SportsShoes/asics.html', {'shoes':shoes})



 