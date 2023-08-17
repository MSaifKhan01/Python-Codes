from django.shortcuts import render, get_object_or_404
import json
from django.core.serializers import serialize
from django.http import JsonResponse, HttpResponse
from .models import Menu

# Create your views here.


def CreateMenu(request):
    if request.method == "POST":
        body = json.loads(request.body)
        dishname = body.get('dishname')
        price = body.get('price')
        available = body.get('available')
        menu = Menu.objects.create(dishname=dishname, price=price, available=available)
    else:
        return HttpResponse(json.dumps({"msg": "wrong routes"}))
    return HttpResponse(json.dumps({"msg": "Data Posted succesfully"}))


'''def GetMenu(req):
    menu = Menu.objects.all()
    respdata=serialize("json",menu)
    return JsonResponse(respdata,safe=False)'''


def GetMenu(req):
    menu = Menu.objects.all()
    # arr = {"data": list(menu.values())}
    arr = serialize('json', menu)
    return JsonResponse(arr, safe=False)


def UpdateMenu(request, itemid):
    print(type(itemid))
    if request.method == "PATCH":
        body=json.loads(request.body)
        available=body.get('available')
        menu = Menu.objects.get(id=itemid)
        menu.available = available
        menu.save()
    else:
        return JsonResponse({"msg":"eror"})
    return JsonResponse({"msg":"Update"})


def DeleteMenu(request, itemid):
    if request.method == "DELETE":
        menu = Menu.objects.get(id=itemid)
        menu.delete()
    else:
        return JsonResponse({"msg":"eror"})
    return HttpResponse(json.dumps({"msg": "Deleted"}))