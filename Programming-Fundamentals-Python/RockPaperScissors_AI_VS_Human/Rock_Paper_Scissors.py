import random
from colorama import Fore, Back, Style

rock = "Rock"
paper = "Paper"
scissors = "Scissors"
player_scores = 0
computer_scores = 0

while True:
    player_move = input(Style.RESET_ALL + "Choose player1: [r]ock,[p]aper or [s]cissors: ")
    if player_move == "r":
        player_move = rock
    elif player_move == "p":
        player_move = paper
    elif player_move == "s":
        player_move = scissors
    else:
        exit("Invalid input. Try again...")
    computer_random_number = random.randint(1, 3)
    computer_move = ""
    if computer_random_number == 1:
        computer_move = rock
    elif computer_random_number == 2:
        computer_move = paper
    elif computer_random_number == 3:
        computer_move = scissors

    print(f"The computer choose: {computer_move}")

    if player_move == rock and computer_move == scissors or \
            player_move == paper and computer_move == rock or \
            player_move == scissors and computer_move == paper:
        print(Fore.BLUE + "Player1 win!")
        player_scores += 1
    elif player_move == computer_move:
        print("Draw")
    else:
        print(Fore.CYAN + "AI win!")
        computer_scores += 1

    again = input(Style.RESET_ALL + "Do you want to play again player1 ? [y]es or [n]o")
    if again == "y":
        print("And you?")
        computer = random.randint(1, 2)
        if computer == 1:
            print(Fore.GREEN + "Yes!")
            continue
        elif computer == 2:
            print(Style.BRIGHT + "I don't want...BYE")
            break
    else:
        print(Fore.LIGHTRED_EX + "Thank you computer for playing with me!")
        break

if player_scores > computer_scores:
    if player_scores > 1:
        print(f"I am the winner with {player_scores} scores.")
    else:
        print(f"I am the winner with only {player_scores} score.")
elif player_scores == computer_scores:
    print("Until next time...")
else:
    if computer_scores > 1:
        print(f"AI is the winner with {computer_scores} scores. ")
    else:
        print(f"AI is the winner with only {computer_scores} score.")
