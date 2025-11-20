from random import choice
from time import sleep


class GreenlightRedlight:
    def __init__(self):
        self.moves = 0
        self.maxmoves = 5

    def startgame(self):
        print("Welcome to Green Light , Red Light")
        print(
            "Type 'move' when it's Green Light, but stay still (type Enter) if you see Red Light!"
        )
        print("Type exit to quit.")

        while self.moves < self.maxmoves:
            getlight = choice(["Green Light", "Red Light"])
            print(f"{getlight}")
            sleep(2)

            if getlight == "Green Light":
                # sleep(2)  # ? Timer => 2 = 2 seconds
                playerreaction = input("Your action: ").lower()
                if playerreaction == "move":
                    self.moves += 1
                    print(f"Good Job! Moves: {self.moves}/{self.maxmoves}")
                elif playerreaction == "exit":
                    print("Thanks for playing the Game...")
                    break
                else:
                    print("Game over!!!, You missed the Green Light.")
                    break
            elif getlight == "Red Light":
                # sleep(2)  # ? Timer => 2 = 2 seconds
                print("<<< RED LIGHT Comming Don't Move >>>")
                playerreaction = input("Your action: ").lower()

                if playerreaction == "move":
                    print("Game over!!!, You died...")
                    break
                elif playerreaction == "exit":
                    print("Thanks for playing the Game...")
                    break

            if self.moves >= self.maxmoves:
                print("Congrats >> You Won !!! <<")


def main() -> None:
    game: GreenlightRedlight = GreenlightRedlight()
    game.startgame()


if __name__ == "__main__":
    main()
