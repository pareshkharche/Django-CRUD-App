from . import views
from django.urls import path

urlpatterns = [
    path("",              views.allemployees, name="allemployees"),
    path("allemployees/", views.allemployees, name="allemployees"),
    path("singleemployee/<int:empid>/", views.singleemployee, name="singleemployee"),
    path("addemployee/",                views.addemployee,    name="addemployee"),
    path("deleteemployee/<int:empid>/",  views.deleteemployee, name="deleteemployee"),
    path("updateemployee/<int:empid>/",  views.updateemployee, name="updateemployee"),
    path("doupdateemployee/<int:empid>/",  views.doupdateemployee, name="doupdateemployee"),



]
