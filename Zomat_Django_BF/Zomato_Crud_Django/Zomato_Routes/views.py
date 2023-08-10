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


