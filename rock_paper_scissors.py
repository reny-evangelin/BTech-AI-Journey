# Rock Paper Scissors....

import random

options = ("rock", "paper", "scissors")
running = True

while running:

    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("Enter the choice (rock, paper, scissors): ")

    print("-------------------")
    print(f"Player : {player}")
    print(f"Computer : {computer}")
        
    if player == computer:
        print("It's a Tie!..")
    elif player == "paper" and computer == "rock":
        print("You Win!..")
    elif player == "scissors" and computer == "paper":
        print("You Win!..")
    elif player == "rock" and computer == "scissors":
        print("You Win!..")
    else:
        print("You Lose!..")
        
    print("-----------------")
    if not input("Play again? (y/n): ").lower() == 'y':
        running = False
           
