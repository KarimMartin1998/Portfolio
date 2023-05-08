print("Welcome to the quiz!")

name = input("Enter your name: ")
while len(name) == 0:
    input("Enter your name: ")
print("Hello "+ name + "! Best of luck on the quiz.")

score = 0

question_1 = input("What is a python?\n"
                   "A. A snake\n"
                   "B. A badger\n"
                   "C. A horse\n"
                   "Enter your answer here (A, B or C): ").upper()

if question_1 == "A":
      print("Correct!")
      score += 1
else:
      print("Incorrect")

question_2 = input("What is the captial of England\n"
                   "A. Gloucester\n"
                   "B. Manchester\n"
                   "C. London\n"
                   "Enter your answer here (A, B or C): ").upper()

if question_2 == "C":
      print("Correct!")
      score += 1
else:
      print("Incorrect")

question_3 = input("What colour is the sky?\n"
                   "A. Green\n"
                   "B. Blue\n"
                   "C. Red\n"
                   "Enter your answer here (A, B or C): ").upper()

if question_3 == "B":
      print("Correct!")
      score += 1
else:
      print("Incorrect")

input("You scored " + str(score) + " out of 3. Thanks for playing!")