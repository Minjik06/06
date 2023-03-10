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
range=[1,2,3,4,5,6]
range1=[1,2,3,4,5,6]
range2=[1,2,3,4,5,6]
i=0
a= int(input("Roll the first dice"))
while i<6:
    ran=random.randint(1,6)
    range[i]=ran
    print(list[i], ran)
    i=i+1
q=0
a= int(input("Roll the second dice"))
while q<6:
    ran=random.randint(1,6)
    range1[q]=ran
    print(list[q], ran)
    q=q+1

o=0
a= int(input("Roll the Third dice"))
while o<6:
    ran=random.randint(1,6)
    range2[o]=ran
    print(list[o], ran)
    o=o+1

k=0
print("final: ")
while k<6:
    v=range[k]+range1[k]+range2[k]
    print(list[k], v)
    k=k+1

