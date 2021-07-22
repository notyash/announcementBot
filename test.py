import random

player1Name = input("Player 1 name: ").upper()
player2Name = input("Player 2 name: ").upper()


class MoveGame:
    def __init__(self):
        self.steps1 = 0
        self.steps2 = 0

    def player_1(self):
        while True:
            answer = input(f'\n{player1Name}: Roll using !roll: ').lower()
            if answer in ["!roll", "!r"]:
                randint_1 = random.randint(1, 6)
                self.steps1 += randint_1
                print(f"You got {randint_1}. You are on {self.steps1} steps.\n")
                break
            else:
                print("Invalid input.")

        return self.steps1

    def player_2(self):
        while True:
            answer = input(f'{player2Name}: Roll using !roll: ').lower()

            if answer in ['!roll', '!r']:
                randint_1 = random.randint(1, 6)
                self.steps2 += randint_1
                print(f"You got {randint_1}. You are on {self.steps2} steps.\n")
                break
            else:
                print("Invalid input.")
        return self.steps2


ob1 = MoveGame()
while True:
    step1 = ob1.player_1()
    if step1 >= 10:
        print(f"{player1Name} Won.")
        break

    step2 = ob1.player_2()
    if step2 >= 10:
        print(f"{player2Name} Won.")
        break
