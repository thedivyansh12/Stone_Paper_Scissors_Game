# S = scissor
# p = paper
# s = stone
import random
def play_game():
    computer = random.choice([-1, 0, 1])
    yourstr = input("enter your choice (s, p, S) : ")
    youdict = {"s" : 1, "p" : -1, "S" : 0}
    reversedict = {1: "STONE", -1 : "PAPER", 0 : "SCISSORS"}
    you = youdict[yourstr]
    print(f"You chose {reversedict[you]}\n Computer chose {reversedict[computer]}")
    if yourstr not in youdict:
        print("Invalid input!")
        return

    if(computer == you):
        print("It's a draw")
    elif((computer - you) == -2 or (computer - you) == 1):
        print("YOU LOSE!!")
    else: 
        print("YOU WIN !")
play_game()
