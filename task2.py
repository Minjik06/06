"""Coin Toss
Ask the player to choose heads or tails.
Toss a coin to determine what the coin will be, and then tell the player if they were correct.
(2 points)"""
import random
frontC="heads"
backC="tails"
list=["heads", "tails"]
ran= random.randint(0,1)
p=0
while p<5:
    ran= random.randint(0,1)
    a= str(input("heads or tails?: "))
    if ran == 0:
        if a == list[ran]:
            print(a, "you are correct")
            p=p+1
        else :
            print(a, "you are wrong")
    else :
        if a == list[ran]:
            print(a, "you are correct")
            p=p+1
        else :
            print(a, "you are wrong")
    print(f"points: {p}")
    

