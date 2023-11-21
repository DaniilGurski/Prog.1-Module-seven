import os
import time
import msvcrt
import random

from bg_colors import bcolors

# # uppgift 1
# while True:

#     user_input = input(":")

#     if user_input == "cl":
#         os.system("cls")
#     elif user_input == "q":
#         break

#     print(user_input)


# # uppgift 2 - se omniscient.py 

# # uppgift 3
# user_name = input("What's your name ?: ")

# print(f"hello {user_name} !\nUse any key (except enter) to exit")

# while True: 
#     if msvcrt.getch() != "\r": # not enter
#         break
#     continue

# # uppgift 4
# print(bcolors.YELLOW + "Module with colors is created and imported !" + bcolors.DEFAULT)


# uppgift 5
# Modules used : bg_colors, random, time
os.system("cls")
colors = {
     1: bcolors.PURPLE,
     2: bcolors.BLUE,
     3: bcolors.CYAN,
     4: bcolors.GREEN,
     5: bcolors.YELLOW,
     6: bcolors.RED
}

while True:
    for index in colors.keys(): 
        new_color = colors[index]
        print(new_color + "hello world :)" + bcolors.DEFAULT)
        time.sleep(1)
        os.system("cls")
