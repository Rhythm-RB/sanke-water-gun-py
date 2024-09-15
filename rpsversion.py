import random

computer =random.randint(0,2)
l = ["rock","paper","scissor"]

def comp():
    print(f"Computer chose {l[computer]}")

a = int(input("Choose your option rock paper or scissor:\n0 for rock 1 for paper and 2 for scissor."))


if(computer == a):
    comp()
    print("Its a Draw")

elif(a==0 and computer==2  or   a==1 and computer==0   or   a==2 and computer==1 ):
    comp()
    print("You won")

else:
    comp()
    print("You Lose")