# Number Guess Application
import random
from array import array
from collections import Counter

winningnum = random.randint(1, 10)
print(winningnum)

gameleft = 5

# store guess using a set for unique
guessset = set()

# store guess using an array
guessarray = array("i", [])

print(f"You have {gameleft} chance to guess the number between 1 and 10.")

for curnumber in range(1, gameleft + 1):
    try:
        guess = int(input(f"Game {curnumber}: Enter Your Guess Number: "))
        # store the guess in the set and array
        guessset.add(guess)
        guessarray.append(guess)
        if guess == winningnum:
            print(
                f"Congratulation! Correct number is {winningnum} in {curnumber} attempts.."
            )
            break
        elif guess < winningnum:
            print("Too low! Try Again.")
        else:
            print("Too high! Try Again..")
    except ValueError:
        print("Invalid input. Please enter a valid number.")
    # check if user has used all chances
    if curnumber == gameleft:
        print(f"Sorry!, You've used all your chances.Winning number is {winningnum}..")

guesstuple = tuple(guessarray)
guesscount = Counter(guessarray)
print("Game Analysis result")
print(f"Your guess unique numbers are = {guessset}")
print(f"Your guess unique numbers are ordered as follows: {guesstuple}")
print(f"Frequency of guess numbers are = {guesscount}")
