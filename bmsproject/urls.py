
from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.demofunction,name="demo"),

    path("demo1",views.demofunction1,name="demo"),
    path("home",views.homefunction,name="home"),
    path("admin project/",views.aboutfunction, name = "about"),
    path("login/",views.loginfunction, name = "login"),
    path("clientlogin/",views.clientlogin, name = "clientlogin"),
    path("employeelogin/",views.employeelogin, name = "employeelogin"),
    path("contactus/",views.contactfunction, name = "contact"),


    path("",include("adminapp.urls")),
    path("",include("clientapp.urls")),
    path("",include("employeeapp.urls")),

]

