from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    from django.http import HttpResponse
    return HttpResponse("Hello, welcome to the home page!")

def profile(request):
    return HttpResponse("This is the profile page.")

def contact(request):
    return HttpResponse("This is the contact page.")

def services(request):
    return HttpResponse("This is the services page.")

def products(request):
    return HttpResponse("This is the products page.")

def about(request):
    return HttpResponse("This is the about page.")

def index(request):
    return render(request, "index.html")

def admin(request):
    return render(request, "admin.html")