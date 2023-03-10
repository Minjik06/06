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


list = ["strength", "intelligence", "wisdom", "dexterity", "constitution", "charisma"]
list1=[0,6]
list2=[0,6]
list3=[0,6]
list4=[0,6]

a=str(input("Roll the first dice: "))


for i in list:
    ran=random.randint(1,6)
    list1.append(ran)
    print(f"{i} {ran}")
a=str(input("Roll the second dice: "))
for h in list:
    ran1=random.randint(1,6)
    list2.append(ran1)
    print(f"{h} {ran1}")
a=str(input("Roll the third dice: "))
for j in list:
    ran2=random.randint(1,6)
    list.append(ran2)
    print(f"{j} {ran2}")
print()


k=list1[0]+list2[0]+list3[0]
kk=list1[1]+list2[1]+list3[1]
kkk=list1[2]+list2[2]+list3[2]
kkkk=list1[3]+list2[3]+list3[3]
kkkkk=list1[4]+list2[4]+list3[4]
kkkkkk=list1[5]+list2[5]+list3[5]
v=list[0]
vv=list[1]
vvv=list[2]
vvvv=list[3]
vvvvv=list[4]
vvvvvv=list[5]
print(f"v {k}")
print(f"vv {kk}")
print(f"vvv {kkk}")
print(f"vvvv {kkkk}")
print(f"vvvvv {kkkkk}")
print(f"vvvvvv {kkkkkk}")