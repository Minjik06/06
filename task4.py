"""Dungeons and Dragons Character Generator
In Dungeons and Dragons, players roll 3 dice to generate statistics for their characters.  The statistics recorded are:
strength
intelligence
wisdom
dexterity
constitution
charisma
Create a character generator that generates a character's statistics
(3 points)"""

import random
list = ["strength", "intelligence", "wisdom", "dexterity", "constitution", "charisma"]
ran=random.randint(0,5)
a=str(input("Enter the \'first\' to roll the dice: "))
print("first dice")
if ran == 0:
    k=list[0]
    print("first statistics recorded are: strength")
    list.pop(0)
elif ran == 1:
    print("first statistics recorded are: intelligence")
    k=list[1]
    list.pop(1)
elif ran == 2:
    print("first statistics recorded are: wisdom")
    k=list[2]
    list.pop(2)
elif ran == 3:
    print("first statistics recorded are: dexterity")
    k=list[3]
    list.pop(3)
elif ran == 4:
    print("first statistics recorded are: constitution")
    k=list[4]
    list.pop(4)
else :
    print("first statistics recorded are: charisma")
    k=list[5]
    list.pop(5)

b=str(input("Enter the \'second\' to roll second dice: "))
print("second dice")
ran=random.randint(0,4)
if ran == 0:
    j=list[0]
    print(f"second statistics recorded are: {list[0]}")
    list.pop(0)
elif ran == 1:
    print(f"second statistics recorded are: {list[1]}")
    j=list[1]
    list.pop(1)
elif ran == 2:
    print(f"second statistics recorded are: {list[2]}")
    j=list[2]
    list.pop(2)
elif ran == 3:
    print(f"second statistics recorded are: {list[3]}")
    j=list[3]
    list.pop(3)
elif ran == 4:
    print(f"second statistics recorded are: {list[4]}")
    j=list[4]
    list.pop(4)

c=str(input("Enter the \'third\' to roll second dice: "))
print("third dice")
ran=random.randint(0,3)
if ran == 0:
    q=list[0]
    print(f"third statistics recorded are: {list[0]}")
    list.pop(0)
elif ran == 1:
    print(f"third statistics recorded are: {list[1]}")
    q=list[1]
    list.pop(1)
elif ran == 2:
    print(f"third statistics recorded are: {list[2]}")
    q=list[2]
    list.pop(2)
elif ran == 3:
    print(f"third statistics recorded are: {list[3]}")
    q=list[3]
    list.pop(3)

print(f"Your characters three statistics are {k}, {j}, {q}")
