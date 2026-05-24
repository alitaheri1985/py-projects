import random

player1_score = 0
player2_score = 0
time = 0
exit = False    
while exit == False:    
    while time < 3:    
            player1 = input("Player 1, please choose an option (rock, paper, scissors): ")
            player2 = random.choice(["rock", "paper", "scissors"])
            if player1 == player2:
                print ("it's a tie!")
            elif player1 == "rock":
                if player2 == "scissors":
                    print("Player 1 wins!")
                    player1_score += 1
                else:
                    print("Player 2 wins!")
                    player2_score += 1
            elif player1 == "paper":
                if player2 == "rock":
                    print("Player 1 wins!")
                    player1_score += 1
                else:
                    print("Player 2 wins!")
                    player2_score += 1
            elif player1 == "scissors":
                if player2 == "paper":
                    print("Player 1 wins!")
                    player1_score += 1
                else:
                    print("Player 2 wins!")
                    player2_score += 1
            else:
                print("Invalid input. Please choose rock, paper, or scissors.")

            time += 1  
    print("")
    print("==========================Game over!=============================")
    print("")
    print(f"Player 1 score: {player1_score}")
    print(f"Player 2 score: {player2_score}")
    score = player1_score - player2_score
    if score > 0:
        print("Player 1 is the winner!")
    elif score < 0:
        print("Player 2 is the winner!")
    else:
        print("It's a tie!")
    play_again = input("Do you want to play again? (yes/no): ")
    if play_again == "no" or play_again == "n":
        exit = True
        print("Thanks for playing!")

    elif play_again == "yes" or play_again == "y":

        player1_score = 0
        player2_score = 0
        time = 0
    else:
        print("Invalid input. Please choose yes or no.")
        