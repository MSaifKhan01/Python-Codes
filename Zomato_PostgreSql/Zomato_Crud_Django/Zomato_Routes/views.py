from django.shortcuts import render,get_object_or_404
import json
from django.core import serializers
from django.http import JsonResponse,HttpResponse

#from .models import FoodItem

from Zomato_Routes.models import FoodItem

def Create(request):
    if request.method=="POST":
        body=json.loads(request.body)
       
        foodname=body['foodname']
        price=body['price']
        available=body['available']
        menu=FoodItem.objects.create(foodname=foodname,price=price,available=available)
    else:
        return HttpResponse(json.dumps({"msg":"wrong routes"}))
    return HttpResponse(json.dumps({"msg":"Data Posted succesfully"}))

def Get(req):
    menu=FoodItem.objects.all()
    arr={"data":list(menu.values())}
    return JsonResponse(arr)



def Update(requestk,itemid):
    menu=get_object_or_404(FoodItem,id=itemid)
    menu.available="yes"
    menu.save()
    return HttpResponse("Updated")

def Delete(request,itemid):
    menu=get_object_or_404(FoodItem,id=itemid)
    menu.delete()
    return HttpResponse(json.dumps({"msg":"Deleted"}))

