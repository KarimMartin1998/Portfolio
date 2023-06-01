import random

max_number = int(input("Enter the maximum range for your guess: "))
computer_guess = random.randint(-1,max_number)
user_guess = input("Guess a number between 1 and "+ str(max_number)+": ")

if user_guess == computer_guess:
    print("Correct!")
else:
    print("Incorrect, I was thinking of " + str(computer_guess))
