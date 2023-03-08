import random
p=0
ran= random.randint(0,2)  # 0 rock, 1 paper, 2 scissor
while p<5:
    ran= random.randint(0,2)
    a= str(input("rock vs paper vs scissors: "))
    if ran == 0:
        if a=="rock":
            print("tie")
            p=p+1
        elif a=="paper":
            print("you win")
            p=p+2
        else:
            print("you lose")
            p=p-0.5
    elif ran == 1:
        if a=="rock":
            print("you lose")
            p=p-0.5
        elif a=="paper":
            print("tie")
            p=p+1
        else:
            print("you win")
            p=p+2
    else:
        if a=="rock":
            print("you win")
            p=p+2
        elif a=="paper":
            print("you lose")
            p=p-0.5
        else:
            print("tie")
            p=p+1
    print("point: ",p)
    ran= random.randint(0,2)
if p>=5:
    print("You got all 5 points")








"""if ran == 0:
    if a=="rock":
        print("tie")
    elif a=="paper":
        print("you win")
    else:
        print("you lose")
elif ran == 1:
    if a=="rock":
        print("you lose")
    elif a=="paper":
        print("tie")
    else:
        print("you win")
else:
    if a=="rock":
        print("you win")
    elif a=="paper":
        print("you lose")
    else:
        print("tie")"""
