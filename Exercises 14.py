#Write a program that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.

def remove_dupes(a):
    commonelements=[]
    for i in a:
        if i not in commonelements:
            commonelements.append(i)
            a.remove(i)
    return commonelements
print(remove_dupes([1,1,1,2,2]))

def remove_dupes_set(a):
    return list(set(a))
print(remove_dupes_set([1,1,1,2,2]))