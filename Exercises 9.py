#Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right
#Extras
#Keep the game going until the user types “exit”
#Keep track of how many guesses the user has taken, and when the game ends, print this out

import random


number = random.randint(1,9)
guess = 0
attempts = 0

while guess != number:
    guess = input("Take a guess: ")
    
    if guess == "exit":
        print ("Goodbye")  
        break
    
    guess = int(guess)
    
    if guess == number:
        attempts += 1
        print ("You got it right in", attempts ,"attempts")
        exit
    elif guess < number:
        attempts += 1
        print ("Try a larger number")
    elif guess > number:
        attempts += 1
        print ("Try a smaller number")
