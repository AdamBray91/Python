#Write a program that takes a list of numbers and makes a new list of only the first and last elements of the given list.

def list_begin_end(a):
    newlist = []
    newlist.append(a[0])
    newlist.append(a[len(a)-1])
    print(newlist)
    
list_begin_end([5, 10, 15, 20, 25])