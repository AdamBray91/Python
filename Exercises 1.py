#Create a program that asks the user to enter their name and their age. 
#Extras
#Print out a message addressed to them that tells them the year that they will turn 100 years old.

name = input("Give me your name: ")
age = int(input("What is your age? "))
year = str(2120-age)
print("Your name is " + name, "and you will be 100 in the year " + year)