#import turtle
from turtle import Turtle, Screen
import random

is_race_on = False # Sets up the game loop
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter: red, green, yellow, orange, blue or purple")
colours = ["red", "green", "yellow", "orange", "blue", "purple"] #list of colours
all_turtles = [] # List of turtle objects


y_axis = -70
for colour in colours:
    new_turtle = Turtle(shape="turtle") # Create a new turtle for each colour
    new_turtle.color(colour) # Change colour to each one in the list
    new_turtle.penup() # Lift pen prior to moving their position
    new_turtle.goto(x=-230, y=y_axis) # Set new position along X-axis and Y-axis
    y_axis = y_axis + 30 #Add 30 to Y-axis variable to move each turtle upwards
    all_turtles.append(new_turtle) # Add turtle objects to the list

if user_bet: # Checks the user has input a colour
    is_race_on = True # Begins game loop is user has made an input

while is_race_on: # While there is a user input:
    for turtle in all_turtles: # Loop through turtle objects in all_turtles list
        if turtle.xcor() > 230: # If one of the turtles X-cord is over 230:
            is_race_on = False  # Stop the loop
            winning_colour = turtle.pencolor() # Save the winning turtle in winning_colour variable
            if winning_colour == user_bet:
                print(f"You've won! The {winning_colour} is the winner")
            else:
                print(f"You've lost! The {winning_colour} is the winner")


        random_distance = random.randint(0, 10)
        turtle.forward(random_distance) # Move all turtles forward a random distance between 0 and 10








screen.exitonclick()