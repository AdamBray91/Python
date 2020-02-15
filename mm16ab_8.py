## Save this file as userid_8.py where userid is *your* userid

## packages
from random import shuffle
from time import perf_counter
import matplotlib.pyplot as plt

## functions

def selectionsort(mylist):
    sortedlist = []
    while len(mylist) > 0:
        lowest = mylist[0]
        for x in mylist:
            if x < lowest:
                lowest = x
        sortedlist.append(lowest)
        mylist.remove(lowest)
    return sortedlist

# add your bubblesort function for (3) here
def bubblesort(mylist):
    n = len(mylist)-1
    for i in range(n,0, -1):
        for j in range(1,i):
            if mylist[j] > mylist[j+1]:
                a = mylist[j]
                mylist[j] = mylist[j+1]
                mylist[j+1] = a
    return mylist
# add the mergesort function (5) here
def mergesort(mylist):
    if len(mylist) <= 1:
        return mylist

    m = len(mylist) // 2
    l = mergesort(mylist[:m])
    r = mergesort(mylist[m:])

    result = []
    i = j = 0
    while (len(result)<len(r)+len(l)):
        if l[i] < r[j]:
            result.append(l[i])
            i = i+1
        else:
            result.append(r[j])
            j = j+1
        if i == len(l) or j == len(r):
            result.extend(l[i:] or r[j:])
            break
    return result
# Write the code described in (1) here  
ivalues = []
times=[]
for i in range(1,11):
    ivalues.append(2**i)
    mylist = list(range(2**i))
    shuffle(mylist)
    time_start = perf_counter()
    selectionsort(mylist)
    time_end = perf_counter()
    total_time = time_end - time_start
    times.append(total_time)
print(times)
    
# Write the code to plot the graph for (2) here,
# and save it as userid_selection.png 
x_values = []
for i in range(1,11):
    x = 2**i
    x_values.append(x)

plt.figure('Selection Plot Times')
plt.loglog(x_values, times, label='Selection')
plt.xlabel('$2^i$ for i $\in$ {1,...,10}')
plt.ylabel('Time')
plt.legend()
plt.show()
plt.savefig('mm16ab_selection.png')
# Write your answer for part (2) here
# (2)
'''The selection sort is O(n**2). This is because for a list of n length you
have to compare the first element to the next n-1 elements, then the next 
element to n-2 and so on until the list is sorted. This is equal to (n-1) + 
(n-2) + (n-3) + ... + 2 + 1 = (n(n-1))/2 = (n**2 - n)/2. 
Therefore selection sort is O(n**2).'''
# Write the code to plot the graph for (4) here
# and save it as userid_bubble.png
ivalues = []
timeb=[]
for i in range(1,11):
    ivalues.append(2**i)
    mylist = list(range(2**i))
    shuffle(mylist)
    time_startb = perf_counter()
    bubblesort(mylist)
    time_endb = perf_counter()
    total_timeb = time_endb - time_startb
    timeb.append(total_timeb)

plt.figure('Selection and Bubble Plot Times')
plt.loglog(x_values, times, label='Selection')
plt.loglog(x_values, timeb, label='Bubble')
plt.xlabel('$2^i$ for i $\in$ {1,...,10}')
plt.ylabel('Time')
plt.legend()
plt.show()
plt.savefig('mm16ab_bubble.png')
# Write the code to plot the graph for (5) here
# and save it as userid_merge.png
ivalues = []
timem=[]
for i in range(1,11):
    ivalues.append(2**i)
    mylist = list(range(2**i))
    shuffle(mylist)
    time_startm = perf_counter()
    mergesort(mylist)
    time_endm = perf_counter()
    total_timem = time_endm - time_startm
    timem.append(total_timem)

plt.figure('Selection, Bubble, and Merge Plot Times')
plt.loglog(x_values, times, label='Selection')
plt.loglog(x_values, timeb, label='Bubble')
plt.loglog(x_values, timem, label='Merge')
plt.xlabel('$2^i$ for i $\in$ {1,...,10}')
plt.ylabel('Time')
plt.legend()
plt.show()
plt.savefig('mm16ab_merge.png')
# Write the code for part (6) here
# and give your answer below
# (6)
ivalues = []
timex=[]
for i in range(1,11):
    ivalues.append(2**i)
    mylist = list(range(2**i))
    shuffle(mylist)
    time_startx = perf_counter()
    mylist.sort()
    time_endx = perf_counter()
    total_timex = time_endx - time_startx
    timex.append(total_timex)
    
plt.figure('Merge and Tim Plot Times')
plt.loglog(x_values, timem, label='Merge')
plt.loglog(x_values, timex, label='Tim')
plt.xlabel('$2^i$ for i $\in$ {1,...,10}')
plt.ylabel('Time')
plt.legend()
plt.show()
plt.savefig('mm16ab_merge+Tim Comparison.png')

'''The bottom line is the time for the Timsort to run, this takes less
time than the merge sort for all values of i'''
# Write your implementation of selection sort (part 7) here
# and give your answer below
# (7)
def selectionsort2(mylist):
    sortedlist = []
    while len(mylist) > 0:
        sortedlist.append(min(mylist))
        mylist.remove(min(mylist))
    return sortedlist
# Write the code for part (8) here
# and give your answer below
# (8)
lengths = []
times = []
for x in range(1,9):
    a = list(range(0,x))
    shuffle(a)
    b = sorted(a)
    start = perf_counter()
    while a != b:
        shuffle(a)
    end = perf_counter()
    timea = end - start
    lengths.append(x)
    times.append(timea)
plt.loglog(lengths, times)
plt.xlabel('Length of List')
plt.ylabel('Time')
plt.axis('tight')

'''The complexity of this is O(n*n!). The n! comes from the fact that for a
list of length n, there are n! possible combinations of the elements each time
the list is shuffled. The n comes from having to check if the list is ordered
each time'''