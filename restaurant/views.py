from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, "home.html")

def menu(request):
    return render(request, "menu.html")

def discount(request):
    return render(request, "discount.html")

def contact(request):
    return render(request, "contact.html")