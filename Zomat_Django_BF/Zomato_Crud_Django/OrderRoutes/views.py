from django.shortcuts import render
import json
from django.http import HttpResponse
order=[]
def CreateOrder(request):
    if request.method=="POST":
        body=json.loads(request.body)
        order.append(body)
    else:
        return HttpResponse({"msg":"Wrong routes"})
    return HttpResponse(json.dumps({"data":"Posted succesfully"}))

def GetOrder(req):
    return HttpResponse(json.dumps({"data":order}))

def Update(req):
    if req.method=="PATCH":
        body=json.loads(req.body)
        id=body['id']
        status=body['status']
        for item in order:
            if item['id']==id:
                item['status']=status
    else:
        return HttpResponse(json.dumps({"msg":"Wrong route"}))
    return HttpResponse(json.dumps({"msg":"Upated Successfully"}))

def Delete(req):
    if req.method=="DELETE":
        body=json.loads(req.body)
        id=body['id']
        for item in order:
            if item['id']==id:
                order.remove(item)
    else:
        return HttpResponse(json.dumps({"msg":"Wrong route"}))
    return HttpResponse(json.dumps({"msg":"Deleted Successfully"}))