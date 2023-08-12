from django.shortcuts import render
import json
from django.http import JsonResponse,HttpResponse

arr=[]

def Create(req):
    if req.method=="POST":
        body=json.loads(req.body)
        arr.append(body)
        print(arr)
    else:
        return HttpResponse("enter wrong req")
    return HttpResponse(json.dumps({"msg":"data posted"}))

def Get(req):
    return HttpResponse(json.dumps({"data":arr}))



def Update(request):
    if request.method=="PATCH":
        body=json.loads(request.body)
        id=body['id']
        for item in arr:
            if item['id']==id:
                item['available']="yes"
    else:
        return HttpResponse("Wrong route")
    return HttpResponse(json.dumps({"msg":"Updated"}))

def Delete(request):
    
    if request.method=="DELETE":
        body=json.loads(request.body)
        id=body['id']
        for item in arr:
            if item['id']==id:
                arr.remove(item)
    else:
        return HttpResponse("Wrong route")
    return HttpResponse(json.dumps({"msg":"Deleted"}))


#def FilterByStatus():
    #return HttpResponse(json.dumps({"data":arr}))


