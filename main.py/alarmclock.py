import time
import webbrowser
import random

alarm=str(raw_input("Enter your alarm time Example=%H:%M:%S format"))
time = time.strftime("%H:%M")
while time !=alarm:
    print ("The time is " + time)

    time.sleep(2)

    if alarm == time:
        print("Wake up!!!")
    else:
        print("You can still sleep")
