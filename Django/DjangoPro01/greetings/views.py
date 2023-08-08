from django.shortcuts import render

from django.http import HttpResponse


# Create your views here.

def Welcome(request):
    return HttpResponse("WellCOME")

def Hello(request,name):
    return HttpResponse(f"Hello {name}")

def Farewell(request,greet):
    return HttpResponse(f"GoodBye {greet}")


