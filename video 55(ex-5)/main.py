import random

computer =random.randint(0,2)
l = ["snake","water","gun"]

def comp():
    print(f"Computer chose {l[computer]}")

a = int(input("Enter snake water or gun:\n0 for snake 1 for water and 2 for gun :"))


if(computer == a):
    comp()
    print("Its a Draw")

elif(a==0 and computer==1  or   a==1 and computer==2   or   a==2 and computer==0 ):
    comp()
    print("You won")

else:
    comp()
    print("You Lose")
    



