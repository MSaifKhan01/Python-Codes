import random
option=["stone","paper","scissor"]

#computer=random.choice(option)

move=True

userCount=0
computerCount=0
TieCount=0

while move:
    computer=random.choice(option)
    user=input("Enter your Move :- ")

    if user not in option:
        print("Enter valid Move ")
    else:
         if user==computer:
                print(f"Computer choice:- {computer}")
                print("Game Tie")
                TieCount+=1
         elif user=="stone" and computer=="scissor":
               print(f"Computer choice:- {computer}")
               print("You won")
               userCount+=1

         elif user=="paper" and computer=="stone":
               print(f"Computer choice:- {computer}")
               print("You won")
               userCount+=1      
              

         elif user=="scissor" and computer=="paper":
               print(f"Computer choice:- {computer}")
               print("You won")
               userCount+=1  

         else:
             print(f"Computer choice:- {computer}")
             print("You Loose")
             computerCount+=1 


         print(f"User-Points:- {userCount}  Computer-Points:- {computerCount}  Game-Tie-Count:-{TieCount}") 


         exit=input("Do you want to Quit Enter (Y/N) :- ")    

         if(exit=="Y" or exit=="y" or exit=="") :
              move=False    