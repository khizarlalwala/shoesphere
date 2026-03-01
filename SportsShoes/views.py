from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'SportsShoes/home.html')
def puma(request):
    return render(request, 'SportsShoes/puma.html')
def adidas(request):
    return render(request, 'SportsShoes/adidas.html')
def asics(request):
    return render(request, 'SportsShoes/asics.html')
def nike(request):
    return render(request, 'SportsShoes/nike.html')