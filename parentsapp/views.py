from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request,"parentsapp/home.html")

def aboutus(request):
    return render(request,"parentsapp/aboutus.html")
 

def services(request):
    return render(request,"parentsapp/services.html")
 

def gallery(request):
    return render(request,"parentsapp/gallery.html")
 

def contactus(request):
    return render(request,"parentsapp/contactus.html")
