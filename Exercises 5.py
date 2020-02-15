#Take two lists and write a program that returns a list that contains only the elements that are common between the lists
#Extras
#Randomly generate two lists to test this

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

commonelements = []
for i in a:
    if i in b:
        commonelements.append(i)
        b.remove(i)
print(commonelements)