from django.http import HttpResponse
from django.shortcuts import render
arr=[]
def Post(request):
    if request.method == "POST":
        name=request.POST.get("name")
        age=request.POST.get("age")
        dict={
            "name":name,
            "age":age
        }
        arr.append(dict)
    return render(request,"create.html")
    
def Get(request):
    print(arr) 
    return render(request,"read.html",{"data":arr})

def Update(request):
    if(request.method=="POST"):
        name=request.POST.get("name")
        value=request.POST.get("value")
        for item in arr:
            if item['name']==name:
                item['name']=value
    return render(request,'update.html')

def Delete(request):
    if request.method=="POST":
        name=request.POST.get("name")
        for item in arr:
            if(item['name']==name):
                arr.remove(item)
    return render(request,"delete.html")
