import json

flag = True
sum = 0


def getOrders():
    print("--------------------------")
    print("     Our Menu       ")
    print("--------------------------")
    with open("Data.json", "r") as file:
        content = file.read()
        arr = json.loads(content)
        for item in arr:
            if item["availability"] == "no":
                continue
            else:
                print(f"id:-{item['id']} name:-{item['name']} price:-{item['price']}")


def UpdateAva():
    itemid = int(input("Enter snacks id:"))
    with open("Data.json", "r") as file:
        content = file.read()
        arr = json.loads(content)
        for item in arr:
            if item["id"] == itemid:
                item["availability"] = "yes"
        with open("Data.json", "w") as file:
            json.dump(arr, file)
        print("--------------------------")
        print("Snacks added to the menu")
        print("--------------------------")


def AddaSnack():
    id = int(input("Enter Snack id:"))
    name = input("Enter Snack name:")
    price = int(input("Enter Snack price:"))
    available = input("is this snack available?(yes/no):")
    with open("Data.json", "r") as file:
        content = file.read()
        arr = json.loads(content)
        arr.append(
            {
                "id": id,
                "name": name,
                "price": price,
                "availability": available
            }
        )
        with open("Data.json", "w") as file:
            json.dump(arr, file)
    print("--------------------------")
    print("Snacks added to the menu")
    print("--------------------------")


def Remove():
    id = int(input("Enter snack id to remove:"))
    with open("Data.json", "r") as file:
        content = file.read()
        arr = json.loads(content)
        for item in arr:
            if item["id"] == id:
                arr.remove(item)
                print("item Deleted Sucessfully")
        with open("Data.json", "w") as file:
            json.dump(arr, file)

def SellSnack(sum):
    id = int(input("Enter snack id to sell:"))
    foodname=input("Enter foodname:")
    name=input("Enter your name:")
    price=0
    with open("Data.json", "r") as file:
        content = file.read()
        arr = json.loads(content)
        for item in arr:
            if item["name"] == foodname:
              price=item['price']
              sum+=price  
    with open("Order.json","r")as file:
        content=file.read()
        arr=json.loads(content)
        arr.append({"orderid":id,"name":name,"price":price,"status":"pending"})
        with open("Order.json", "w") as file:
            json.dump(arr, file)
    print("--------------------------")
    print("Snacks selled succesfully")
    print("--------------------------")
    return sum


def UpdateStatus():
    id = input("Enter id to update status of snack:")
    change = input("enter that want to change:")
    with open("Order.json", "r") as file:
        content = file.read()
        arr = json.loads(content)
        for item in arr:
            if item["orderid"] == id:
                item["status"] = change
        with open("Order.json", "w") as file:
            json.dump(arr, file)
    print("--------------------------")
    print("Snacks Status Updated succesfully")
    print("--------------------------")

def FilterByStatus():
    filter=input("Enter The status to get data:")
    with open("Order.json", "r") as file:
        content = file.read()
        arr = json.loads(content)
        for item in arr:
            if item['status']==filter:
                print(f"orderid:-{item['orderid']}")
                print(f"name:-{item['name']}")
                print(f"price:-{item['price']}")
                print(f"status:-{item['status']}")
                print("-------------------------------------")
            else:
                print("No data Available with this status ")


            



while flag:
   
    print("--------------------------")
    print("ZOMATO")
    print("--------------------------")

    print("1. Display Menu")
    print("2. Update Availablity")
    print("3. Add a snack")
    print("4. Remove a Snack")
    print("5. Buy a Snack")
    print("6. Total Sale")
    print("7. Update Status of Snack")
    print("8. Filter by Status")
    userinput = int(input("Enter the Number to get Details:"))
    if userinput == 1:
        getOrders()
    elif userinput == 2:
        UpdateAva()
    elif userinput == 3:
        AddaSnack()
    elif userinput == 4:
        Remove()
    elif userinput == 5:
        sum+=SellSnack(sum)
    elif userinput == 6:
        print("--------------------------")
        print(f"Total sale:- {sum}")
        print("--------------------------")
    elif userinput==7:
        UpdateStatus()
    elif userinput==8:
        FilterByStatus()
    out = input("Do you want to Quit? (Y/N):")
    if out == "Y" or out == "y":
        flag = False