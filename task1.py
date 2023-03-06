"""Number Guessing Game
Have the computer generate a random number from 1 to 100.  The players will try to guess the number, and the computer will tell them if they are too high or too low.  Play continues until they guess correctly at which point the computer tells them how many guesses it took.
(2 points) """
import random
a=str(input("Enter a user name: "))
print("Start the game")
ran= random.randint(1,100)
print("random numer is chosen, enter the number from 1 to 100")
b=int(input("1 guess: "))
if b==ran:
    print("congratulations, you got the answer")
else:
    print("wrong answer")
    if b<ran:
        print("random numer is bigger than your answer")
    else:
        print("random number is smaller than your answer")
k=int(input(" guess again: "))
while ran!=k:
    if k<ran:
        print("try again, random number is bigger than your answer")
    elif k>ran:
        print("try again, random nuber is smaller than your answer")
    k=int(input(" guess again: "))
print("finally you got the answer")
