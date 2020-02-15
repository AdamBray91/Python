import matplotlib.pyplot as plt
from collections import Counter

#Generates a list of primes up to n
def eratosthenes(n):
    primes = list(range(2,n))
    for i in primes:
        j = 2
        while i*j <= primes[-1]:
            if i*j in primes:
                primes.remove(i*j)
            j=j+1
    return primes
    
#Checks that all evens greater than 4 and less than n can be made with
#combinations of primes i and j. To speed up my code, I would have a way to
#stop checking for prime sums when at most 1 has been found but also count the
#amount of ways an even number can be made.
def evens_sum(n):
    evens = list(range(6,n+1,2))
    primes = eratosthenes(n)
    evensumlist=[]
    evens2=[]
    for a in evens:
        for i in primes:
            for j in primes:
                if i <= j:
                    if a == i + j:
                        evensumlist.append([a,i,j])
                        evens2.append(a)
    for b in evens:
        if b not in evens2:
            print(b," is not in the list of evens")
    return evensumlist, evens2

#x values are the even Numbers from 6 to n, y values are the number of
#occurances of each even number from the list evens2 in evens_sum.
def evens_primes_plot(n):
    x = []
    y = []
    for a in list(range(6,n+1,2)):
        y.append(Counter(evens_sum(n)[1])[a])
        x.append(a)
    
    a = plt.scatter(x, y)
    plt.xticks(x)
    plt.yticks(y)
    return a  

#Checks that all odd numbers greater than 5 to n can be made with the sum of
#a prime i and double a prime j.
def odd_sum(n):
    odds = list(range(7,n+1,2))
    primes = eratosthenes(n)
    oddsumlist = []
    odds2 = []
    for a in odds:
        for i in primes:
            for j in primes:                
                if a == i + j + j:
                    oddsumlist.append([a,i,j,j])
                    odds2.append(a)
    for b in odds:
        if b not in odds2:
            print(b," is not in the list of odds")
    return oddsumlist

#Generates a list of Odd composite numbers from 9 to n
def composite_numbers(n):
    primes = eratosthenes(n)
    odds = list(range(3,n,2))
    for p in primes:
        if p in odds:
            odds.remove(p)
    composites = odds
    return composites

#Checks that a composite number c can be made from p+2*s where p is a prime
#from the list primes and s is square numbers from 1 to 10000
def composite_checker(primes,c):
    squares = list(i**2 for i in range(1,100))
    for p in primes:
        for s in squares:
            if p+2*s == c:
                return c
            else:
                continue

#Checks that all odd composite numbers from 9 to 10000 can be made from the sum
#of a prime and double a square. The smallest value of c where this doesn't hold
#is 5777.
def conjecture3():
    while True:
        primes = eratosthenes(10000)
        for c in composite_numbers(10000):
            if composite_checker(primes,c) == c:
                continue
            else:
                return c, "is the smallest odd composite not of the form p+2*s"
                break
print(conjecture3())