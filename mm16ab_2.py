# Template file for Week 2
# Lines that start with '#'
# are comments and are ignored
# by Python.

# Insert your Euclid algorithm program lines here:

    #i
a=105
b=24
while b > 0:
    t=b
    b=a%b
    a=t
gcd_i = a
print('Gcd(105,24) =',gcd_i)

#ii
a=6024
b=1284
while b > 0:
    t=b
    b=a%b
    a=t
gcd_ii = a
print('Gcd(6024,1284) =',gcd_ii)

#iii
a=98777
b=12945
while b > 0:
    t=b
    b=a%b
    a=t
gcd_iii = a
print('Gcd(98777,12945) =',gcd_iii)

# Give the answers to the questions below:
# gcd(105,24) = 3 
# gcd(6024,1284)= 12 
# gcd(98777,12945) = 1

# Insert your Extended Euclid algorithm program here:

a, b = 6024, 1284
x, xprev, y, yprev = 0, 1, 1, 0
while b > 0:
    q = a//b
    a, b = b, a%b
    x, xprev = xprev - q*x, x
    y, yprev = yprev - q*y ,y
print('Gcd(6024,1284)=',xprev,'* 6024 +', yprev,'*1284 =',a)

# Insert your counting-steps Euclid program here:

from math import log, pi
a=105
b=24
i=0
while b > 0:
    i=i+1
    t=b
    b=a%b
    a=t
gcd = a
print('Gcd(105,24) =',gcd)
print('Number of steps =', i)
print('Average number of digits in a =', 5*log(105,10))
print('Average number of steps required =', (12*log(105)*log(2))/pi**2)

# Give examples of a,b which produce larger
# and smaller number of steps than the average
# here:
    
from math import log, pi
a=105
b=25
i=0
while b > 0:
    t=b
    b=a%b
    a=t
    i=i+1
gcd = a
print('Gcd(105,25) =',gcd)
print('Number of steps=',i)
print('Average number of steps required =', (12*log(105)*log(2))/pi**2)
if i < (12*log(105)*log(2))/pi**2:
    print(i, '<', (12*log(105)*log(2))/pi**2)
    
a=105
b=23
i=0
while b > 0:
    t=b
    b=a%b
    a=t
    i=i+1
gcd = a
print('Gcd(105,23) =',gcd)
print('Number of steps=',i)
print('Average number of steps required =', (12*log(105)*log(2))/pi**2)
if i > (12*log(105)*log(2))/pi**2:
    print(i, '>', (12*log(105)*log(2))/pi**2)

#Verifying Maximum for a and b when a and b are fibonacci numbers

from math import log, pi, floor
a1=34
b=21
i1=0
while b > 0:
    i1=i1+1
    t=b
    b=a1%b
    a1=t
gcd1 = a1
print('Gcd(34,21) =',gcd1)
print('Number of steps=',i1)
print('Average number of digits in a =', 5*log(34,10))
if i1 == floor(5*log(34,10)):
    print(i1, 'is roughly', 5*log(34,10), 'and a=34 and b=21 are consecutive Fibonacci numbers so Lames Theorem holds')
else:
    print(i1, 'is not roughly', 5*log(34,10), 'but are consecutive Fibonacci numbers so Lames Theorem does not hold')