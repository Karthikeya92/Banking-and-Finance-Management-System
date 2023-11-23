from django.http import HttpResponse
from django.shortcuts import render


def demofunction(request):
    return HttpResponse('<h1 style="text-align: center; color: blue;"><u>PFSD PROJECT</u></h1>')

def demofunction1(request):
    return HttpResponse("<h3>K L University</h3>")


def homefunction(request):
    return render(request,"index.html")


def aboutfunction(request):
    return render(request,"about.html")

def loginfunction(request):
    return render(request,"login.html")

def contactfunction(request):
    return render(request,"contact.html")



def clientlogin(request):
    return render(request,"clientlogin.html")


def employeelogin(request):
    return render(request,"employeelogin.html")








