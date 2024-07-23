"""Rock Paper Scissors by Anna"""

import random

t = ["✊", "✋" ,"✌"]

print("====================\nRock Paper Scissors\n===================")

player = int(input(" 1) ✊\n 2) ✋\n 3) ✌\n Pick a number: ")) - 1


computer = random.randint(0,2)

print(f"You chose: {t[player]}")
print(f"CPU chose: {t[computer]}")

if player == computer:
    print("It's a tie!")
elif (player == 0 and computer == 2) or \
     (player== 1 and computer== 0) or \
     (player== 2 and computer== 1):
    print("The player won!")
else:
    print("You lose.")






