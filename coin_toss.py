# This python code is a game where two players are randomly playing a
# coin toss game.

import random
player_1 = input("Player_1 choose either Head or Tail:- ")
if player_1.upper() == "HEAD":
    player_2 = "tail"
else:
    player_2 = "head"
print("PLAYER_1 choosed " +  player_1)
print("PLAYER_2 choosed " +  player_2)
a = ["head", "tail"]
result = random.choice(a)
print("The result of the coin toss is " + result)
print(" ")
if result.upper() == player_1:
    print("PLAYER_1 WON THE GAME")
else:
    print("PLAYER_2 WON THE GAME")