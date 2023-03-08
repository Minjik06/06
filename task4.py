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
a=str("Enter the k to roll the dice")
print("first dice")
if ran == 0:
    k=list[0]
    print("first statistics recorded are: strength")
    list.remove[0]
elif ran == 1:
    print("first statistics recorded are: intelligence")
    k=list[1]
    list.remove[1]
elif ran == 2:
    print("first statistics recorded are: wisdom")
    k=list[2]
    list.remove[2]
elif ran == 3:
    print("first statistics recorded are: dexterity")
    k=list[3]
    list.remove[3]
elif ran == 4:
    print("first statistics recorded are: constitution")
    k=list[4]
    list.remove[4]
else :
    print("first statistics recorded are: charisma")
    k=list[5]
    list.remove[5]

