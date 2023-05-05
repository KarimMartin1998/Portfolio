import random

while True:
    list = ["rock", "paper", "scissors"]

    answer = input("Rock, Paper, Scissors? ").lower()
    compAnswer = random.choice(list)
    print("I choose {}".format(compAnswer))

    if answer == compAnswer:
        print("Draw!")
    elif answer == "rock" and compAnswer == "scissors":
        print("You win!")
    elif answer == "rock" and compAnswer == "paper":
        print("You lose!")
    elif answer == "scissors" and compAnswer == "rock":
        print("You lose!")
    elif answer == "scissors" and compAnswer == "paper":
        print("You win!")
    elif answer == "paper" "paper" and compAnswer == "rock":
        print("You win!")
    elif answer == "paper" and compAnswer == "scissors":
        print("You lose!")
    else:
        print("That's not an answer! Try again!")

    play_again = input("Play again? (yes/no) ").lower()
    if play_again != "yes":
        break

print("Bye!")