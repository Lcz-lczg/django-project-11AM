from django.shortcuts import render
from django.http import HttpResponse
from .models import Contact

def home(request):
    if request.method=="POST":
        obj = Contact(name=request.POST['txtname'],phoneno=request.POST['txtphone'],email=request.POST['txtemail'],message=request.POST['txtmsg'])
        obj.save()
        return render(request,"parentsapp/index.html",{"key":"Registration successfully"})

    return render(request,"parentsapp/index.html")

def aboutus(request):
    data = Contact.objects.all()
    return render(request,"parentsapp/about.html",{'key':data})
 

def services(request):
    return render(request,"parentsapp/services.html")
 

def gallery(request):
    return render(request,"parentsapp/gallery.html")
 

def contactus(request):
    return render(request,"parentsapp/contactus.html")
