from django.shortcuts import render
from django.http import HttpResponse
def hello(request):
    return HttpResponse("<h1>Hello World</h1>")

def studentinfo(request):
    return render(request,"guestapp/student.html")

def studentoutput(request):
    name =request.GET["txtname"]
    email = request.GET["txtemail"]
    contact = request.GET["txtcontact"]
    address = request.GET["txtaddress"]
    return HttpResponse("name is "+name + " <hr> email is "+email + "<hr> contact  is "+contact + " <hr> address is "+address);
def addition(request):
    return render(request,"guestapp/addition.html")

def additionoutput(request):
    num1 = request.GET["txtnum1"]
    num2 = request.GET["txtnum2"]
    c = int(num1)+int(num2)
    return HttpResponse("Result is "+str(c))
    