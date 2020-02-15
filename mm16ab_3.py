# Template file for Week 3
# Lines that start with '#'
# are comments and are ignored
# by Python.

# 3A Write your functions below
# E.g.,
def cubed(x):
    xxx = x**3
    return xxx
print(cubed(3))

def mean(x,y):
    return (x+y)/2
print(mean(4,5))

def pyth(a,b,c):
    x = a**2 + b**2
    y = c**2
    if x == y:
        return True
    else:
        return False
pyth(3,4,5)

def meanlist(x):
    return(sum(x)/len(x))
print(meanlist([1,2,3,4,5,6,7,8,9]))

def gcd(a,b):
    while b > 0:
        t = b
        b = a % b
        a = t
    return(a)
print(gcd(12,36))

def Binary(a):
    binary = []
    while a > 0:
        binary.append(a%2)
        a = a//2
    binary.reverse()
    return(binary)
Binary(6)

def Decimal(a):
    decimal = 0
    a.reverse()
    for i in range(len(a)):
        decimal = decimal + a[i]*(2**i)
    return(decimal)
Decimal([1,1,0])

from math import floor
def day(d,m,Y, C):
    x=(d+(13/5)*(m+1)+Y+Y/4+C/4-2*C)%7
    days = ['Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    return(days[floor(x)])
print(day(16,10,17,20))
# 3B Write your Eratosthenes function below

def eratosthenes(max):
    primes = list(range(2,max+1))
    for i in primes:
        j = 2
        while i*j <= primes[-1]:
            if i*j in primes:
                primes.remove(i*j)
            j = j + 1
        return primes
print(eratosthenes(100))

# Answer the questions as comments below:
# 100th prime is: 199
# 2000th prime is: 4001
# Primes between 3000 and 30000: 13500

# 3C Write your Sundaram function below:
def sundaram(n):
    primes = list(range(2,n))
    for j in range(1,n+1):
        for i in range(1,j+1):
            if i+j+2*i*j in primes:
                primes.remove(i+j+2*i*j)
    primes2 = [2*x + 1 for x in primes]
    return(primes2)
print(sundaram(20))



