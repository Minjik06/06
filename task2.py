"""Coin Toss
Ask the player to choose heads or tails.
Toss a coin to determine what the coin will be, and then tell the player if they were correct.
(2 points)"""
import random
a= str(input("heads or tails?: "))
frontC="heads"
backC="tails"
ran= random.randint(0,1)
if ran == 0:
    ran = frontC
    if ran == a:
        print(ran, "you are correct")
    else :
        print(ran, "you are wrong")
else :
    ran = backC
    if ran == a:
        print(ran, "you are correct")
    else :
        print(ran, "you are wrong")

