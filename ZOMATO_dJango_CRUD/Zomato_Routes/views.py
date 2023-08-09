from django.shortcuts import render

# Create your views here.
arr = []

order=[]

sum=0


def Create(request):

    if request.method == "POST":

        id=request.POST.get('id')
        name = request.POST.get("name")
        price = request.POST.get("price")
        available = request.POST.get("available")
        dict = {"id":id,"name": name, "price": price, "available": available}
        arr.append(dict)
    return render(request, "CreateDish.html")


def Get(request):

    arr1=[]
    for item in arr:

        if item['available']=="yes":
            arr1.append(item)
    return render(request, "ReadMenu.html", {"data": arr1})

def Update(request):

    if request.method=="POST":

        id=request.POST.get("id")
        for item in arr:

            if(item['id']==id):

                item['available']="yes"
    return render(request,"UpdateStatus.html")

def Delete(request):

    if request.method=="POST":

        id=request.POST.get("id")
        print(id)
        for item in arr:

            if(item['id']==id):

                arr.remove(item)
    return render(request,"DeleteDish.html")

def Userorder(request):

    if request.method=="POST":

        name=request.POST.get("name")
        food=request.POST.get("food")
        dict={"name":name,"food":food,"status":"pending"}
        order.append(dict)
    return render(request,"Order.html")

def orderGet(request):

    return render(request, "ViewOrder.html", {"data": order})