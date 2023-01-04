import random

user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors"]

while True:
    user_input = input(" Enter Rock/Paper/Scissors or Q to quit: ").lower()

    if user_input == "q":
        break

    if user_input not in options:  # if an input exist in this string of inputs
        continue  # start while loop againq

    random_number = random.randint(0, 2)   # rock: 0, paper: 1, scissors: 2

    computer_pick = options[random_number]

    print("Coputer picked", computer_pick + ".")

    if user_input == "rock" and computer_pick == "scissors":
        print("You Won!!")
        user_wins += 1
        continue

    elif user_input == "paper" and computer_pick == "rock":
        print("You Won!!")
        user_wins += 1
        continue

    elif user_input == "scissors" and computer_pick == "paper":
        print("You Won!!")
        user_wins += 1
        continue

    else:
        print("You Lost!")
        computer_wins += 1


print("You won", user_wins, " times")
print("The computer won", computer_wins, " times")
print("Goodbye!")
