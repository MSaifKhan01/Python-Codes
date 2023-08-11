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



def Update(req,itemid):
    menu=get_object_or_404(FoodItem,id=itemid)
    if(req.method=="PATCH"):
        
         if(menu.available=="yes"):
            menu.available="no"
         else:
            menu.available="yes"  

    else:
        return JsonResponse({"msg":"eror"})          
    
    menu.save()
    return HttpResponse(json.dumps({"msg":"Updated"}))

def Delete(request, itemid):
    if request.method == "DELETE":
        menu = get_object_or_404(FoodItem, id=itemid)
        menu.delete()
    else:
        return JsonResponse({"msg":"eror"})
    return HttpResponse(json.dumps({"msg": "Deleted"}))

