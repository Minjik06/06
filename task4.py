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
def dice():
    for i in list:
        ran=random.randint(1,6)
        print(f"{i} {ran}")
a=str(input("Roll the first dice: "))
dice()
a=str(input("Roll the second dice: "))
dice()