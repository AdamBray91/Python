#Write a password generator in Python

import random

strength = str(input("Enter difficulty of password, either 'easy' or 'hard': ",))

characters=['apple','orange','pineapple','pear','lemon','lime']
characters2="1abcdefghijklmnopqrstuvwxyz0123456789"
password = []
if strength == "easy":
    print(characters[random.randint(0,5)])
elif strength == "hard":
    length = int(input("Enter desired length of password: ",))
    i = 0
    while i < length:
        password.append(characters2[random.randint(0,35)])
        i = i + 1
    print("".join(password))