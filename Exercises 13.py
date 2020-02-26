#Write a program that asks the user how many Fibonnaci numbers to generate and then generates them.

length = int(input("Enter number of Fibonnaci numbers to generate: ",))

list = [1,1]
if length == 0:
    print([])
if length == 1:
    print([1])
elif length > 1:
    while len(list) < length:
        list.append(list[-1]+list[-2])
    print(list)