# Rock, Paper, Scissors Game
import random 

while True:
    Player = input("Enter a choice (rock, paper, scissors, end the game):")
    possible_action = ["rock", "paper", "scissors", "end the game"]
    CPU = random.choice(possible_action)
    print(f"\nYou chose {Player}, computer chose {CPU}.\n")
    
    if Player == CPU:
        print(f"Both players selcted {Player}. It's a tie!")
    elif Player == "rock":
        if CPU == "scissors":
            print("Player(rock): CPU(scissors) rock smashes scissors!, You win!")
        else:
            print("Player(rock): CPU(paper) Paper covers rock! You lose!")
    elif Player == "paper":
        if CPU == "rock":
            print("Player(Paper): CPU(rock) paper covers rock! You win!")
        else:
            print("Player(Paper): CPU(scissors) scissors cuts paper! You lose!")
    elif Player == "scissors":
        if CPU == "paper":
            print("Player(scissors): CPU(paper) scissors cuts paper! You win!")
        else:
            print("Player(scissors): CPU(rock) rock smashes scissors!, You lose!")

    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break

         