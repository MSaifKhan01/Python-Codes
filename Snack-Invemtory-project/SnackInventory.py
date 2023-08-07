import json
flag=True
sum=0
while flag:
    print("|--|------ Mumbai Munchies ------|--|")
    print("1. Display Menu")
    print("2. Update Menu")
    print("3. Add a snack")
    print("4. Remove a Snack")
    print("5. Sell a Snack")
    print("6. Total Sale")
    userinput=int(input("Enter the Number to get Details:"))
    if(userinput==1):
        print("--------------------------")
        print("Our Menu")
        print("--------------------------")
        with open("Data.json","r") as file:
            content=file.read()
            arr=json.loads(content)
            for item in arr:
                if item['availability']=="no":
                    continue
                else:
                    print(f"id:-{item['id']} name:-{item['name']} price:-{item['price']}")
    elif userinput==2:
        itemid=int(input("Enter snacks id:"))
        with open("Data.json","r") as file:
            content=file.read()
            arr=json.loads(content)
            for item in arr:
                if item['id']==itemid:
                    if item['availability']=="yes":
                        item['availability']="no"
                    else:
                        item['availability']="yes"    
            with open("Data.json","w") as file:
               json.dump(arr,file)
            print("--------------------------")
            print("Snacks added to the menu")
            print("--------------------------")
    elif userinput==3:
        id=int(input("Enter Snack id:"))
        name=input("Enter Snack name:")
        price=int(input("Enter Snack price:"))
        available=input("is this snack available?(yes/no)")
        with open("Data.json","r") as file:
            content=file.read()
            arr=json.loads(content)
            arr.append({"id":id,"name":name,"price":price,"availability":available})
            with open("Data.json","w") as file:
               json.dump(arr,file)
        print("--------------------------")
        print("Snacks added to the menu")
        print("--------------------------")
    elif userinput==4:
        id=int(input("Enter snack id to remove:"))
        with open("Data.json","r") as file:
            content=file.read()
            arr=json.loads(content)
            for item in arr:
                if(item['id']==id):
                    arr.remove(item)
            with open("Data.json","w") as file:
               json.dump(arr,file)
    elif userinput==5:
        id=int(input("Enter snack id to sell:"))
        with open("Data.json","r") as file:
            content=file.read()
            arr=json.loads(content)
            if(len(arr)>0):
                 for item in arr:
                    if(item['id']==id):
                        sum+=item['price']
                        arr.remove(item)
                        with open("Data.json","w") as file:
                            json.dump(arr,file)
                            print("--------------------------")
                            print("Snacks selled succesfully")
                            print("--------------------------")
                    else:
                        print("put Right id") 
            else:
                print("no data available")  
                     
                         
    elif userinput==6:
        print("--------------------------")
        print(f"Total sale-Price:- {sum}")
        print("--------------------------")
    out=input("Do you want to Quit? (Y/N):")
    if(out=="Y" or out=="y"):
       flag=False
