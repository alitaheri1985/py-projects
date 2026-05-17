import random


exit = False
while exit == False:

    player_1 = input("Player 1, please choose an option (rock, paper, scissors): ")

    pc = random.choice(["rock", "paper", "scissors"])

    print(f"player 1 chose {player_1}")
    print(f"pc chose {pc}")

    if player_1 == '1':
        break
    elif player_1 == pc:
        print("It's a tie!")
    elif player_1 == "rock":
        if pc == "scissors":
            print("Player 1 wins!")
        else:
            print("PC wins!")
    elif player_1 == "paper":
        if pc == "rock":
            print("player_1 wins!")
        else:
            print("PC wins!")
    elif player_1 == "scissors":
        if pc == "paper":
            print("Player 1 wins!")
        else:
            print("PC wins!")
    else:
        print("invalid input. Please choose rock, paper, or scissors.")
    
    exit = input ("Do you want to play again? (yes/no)")
    
    if exit == "no":
        exit = True
    else:
        exit = False
print("Thanks for playing!")