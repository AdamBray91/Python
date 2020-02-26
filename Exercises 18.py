#Create a program that will play the “cows and bulls” game with the user

import random

#def compare(number, guess):
#    cow = [0,0]
#    for i in range(0,len(number)):
#        if guess[i] == number[i]:
#            cow[0] += 1
#        elif guess[i] != number[i]:
#            cow[1] += 1
#    return cow
    
def compare(number, guess):
    cow = [0,0]
    for i in number:
        if i in guess:
            if guess.index(i)==number.index(i):
                cow[0] += 1
            else:
                cow[1] += 1
    return cow

if __name__=="__main__":
    number = str(random.randint(0,10000))
    print(number)
    
    play = True
    guesses = 0  
    
    while play:
        guess = str(input("Take a guess: ",))
        count = compare(number, guess)
        guesses += 1  
        if count[0] == 4:
            play == False
            print("Well done! The number was", number,". You got it after", guesses,"guesses.")
            break
        else:          
            print("Not quite. You have",count[0],"cows and",count[1],"bulls. You have had", guesses," guesses.")
