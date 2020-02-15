#Take a list and write a program that prints out all the elements of the list that are less than 5.
#Extras:
#Instead of printing the elements one by one, make a new list that has all the elements less than 5 from this list in it and print out this new list.
#Write this in one line of Python.
#Ask the user for a number and return a list that contains only elements from the original list a that are smaller than that number given by the user.


list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
newlist = []
for i in list:
    if i <= 5:
        newlist.append(i)
print(newlist)

number = int(input("Input a number to find numbers smaller than given number: "))
newlist2 = []
for i in list:
    if i < number:
        newlist2.append(i)
print(newlist2)