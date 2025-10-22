# Number Guess Application
import random

winningnum = random.randint(1, 10)
print(winningnum)

gameleft = 5

print(f"You have {gameleft} chance to guess the number between 1 and 10.")

for curnumber in range(1, gameleft + 1):
    try:
        guess = int(input(f"Game {curnumber}: Enter Your Guess Number: "))
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
    if curnumber == gameleft:
        print(f"Sorry!, You've used all your chances.Winning number is {winningnum}..")
