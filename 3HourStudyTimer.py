"""Simple 3-hour study timer app that requests an input and starts a
countdown, pausing for every 25 minutes with a 5-minute break before
continuing"""

from playsound import playsound
import time

print("Welcome to the study timer!")
hours = int(input("How many hours do you wish to study for? "))


# Function that shows what happens after 25 minutes
def break_time():
    playsound("C:\\Users\\karim\\Downloads\\bell.wav")  # URL to custom sound played.
    print("Break time, listen out for the bell to start again!")
    time.sleep(300)  # Timer sleeps for 5 minutes.
    playsound("C:\\Users\\karim\\Downloads\\bell.wav")
    print("And we're off!")  # Timer starts when sound is played.


# Countdown function.
def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        hours, mins = divmod(mins, 60)
        timer = '{:02d}:{:02d}:{:02d}'.format(hours, mins, secs)  # Formatting the timer.
        print(timer)  # Prints the timer to the console.
        time.sleep(1)  # Sleeps for 1 second.
        t -= 1  # Takes a second off of t, completing the countdown.

        if hours == 0:  # If user selects one hour
            if t == 2100 or t == 600:  # If time is 35 or 10 minutes
                break_time()  # Run this function. Same steps repeated for 2 / 3 hours.

        if hours == 1:
            if t == 5700 or t == 4200 or t == 2700 or t == 1200:
                break_time()

        if hours == 2:
            if t == 9300 or t == 7800 or t == 6300 or t == 4800 or t == 3300 or t == 1800 or t == 300:
                break_time()

    print("Study time over!")  # Once loop finished, study time is over.
    playsound("C:\\Users\\karim\\Downloads\\bell.wav")  # Play sound, signifying the end.


t = hours * 3600  # Variable converts time into hours.
countdown(int(t))  # Begins the countdown.