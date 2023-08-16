print("Welcome to the number guessing game!")
print("I'm thinking of a number between 1 and 100")

import random
def number_guess():
  number = random.randint(1,100)
  return number

computer_guess = number_guess()
print(f"Hint: I'm thinking of {computer_guess}")

lives = 0

def easy():
  return lives + 10

def hard():
  return lives + 5

def remove_life():
  return lives - 1

difficulty = input("Choose a mode, type 'easy' or 'hard': ").lower()
if difficulty == "easy":
  lives = easy()
if difficulty == "hard":
  lives = hard()


print(f"You have {lives} attempts to guess the number.")

while lives != 0:
  user_guess = int(input("Make a guess: "))
  if user_guess == computer_guess:
    print(f"Correct! The answer was {computer_guess}!")
  if user_guess > computer_guess:
    print("Too high.")
    lives = remove_life()
    print(f"You have {lives} lives remaining.")
  if user_guess < computer_guess:
    print("Too low.")
    lives = remove_life()
    print(f"You have {lives} lives remaining.")

if lives == 0:
  print(f"Game over! I was thinking of {computer_guess}")
