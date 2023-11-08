import os
import time

os.system("cls")
print("Welcome to the OMNISCIENT program\nI will guess your name, in a matter of seconds...\n")

user_name = input("Name you want me to guess:")

loading_phrases = ["Searching for your name in the quantum realm...", "Collecting some energy from Proxima Centauri...", "Summoning the name gods for a grand reveal..."]
loading_animation = ["/", "-","\\", "|"]

for phrase in loading_phrases:
    for frame in loading_animation:
        os.system("cls")
        print(phrase)
        print(frame)
        time.sleep(.5)

print("And your name is...")
time.sleep(1)
print(user_name,end="!")