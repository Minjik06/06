"""
Advanced Dungeons and Dragons
optional rolling systems include:
a) roll 4 dice, discard the lowest
b) roll 3 dice, reroll 1's.
Add these as options to your D&D Character Statistics Generator
"""
import random
list = ["strength", "intelligence", "wisdom", "dexterity", "constitution", "charisma"]
range=[1,2,3,4,5,6]
range1=[1,2,3,4,5,6]
range2=[1,2,3,4,5,6]
range3=[1,2,3,4,5,6]
i=0
a= int(input("Roll the first dice"))
while i<6:
    ran=random.randint(1,6)
    range[i]=ran
    print(list[i], ran)
    i=i+1
print("\n")
k=0
q=0
a= int(input("Roll the second dice"))
while q<6:
    ran=random.randint(1,6)
    range1[q]=ran
    print(list[q], ran)
    q=q+1
print("\n")
k=0
o=0
a= int(input("Roll the Third dice"))
while o<6:
    ran=random.randint(1,6)
    range2[o]=ran
    print(list[o], ran)
    o=o+1
print("\n")
c=0
a= int(input("Roll the Fourth dice"))
while c<6:
    ran=random.randint(1,6)
    range2[c]=ran
    print(list[c], ran)
    c=c+1
print("\n")
k=0
print("final: ")
while k<6:
    v=range[k]+range1[k]+range2[k]
    print(list[k], v)
    k=k+1


