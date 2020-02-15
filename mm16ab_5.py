# import files here
from math import sin, cos, sqrt, atan, pi
# 5A 
#(1)
def cube(x):
    return x**3

#(2)
def sum_dif(x,y):
    return x + y, abs(x-y)

#(3)
def sin2_cos2(x):
    return 1

#(4)
def fib(n):
    fib=[0,1]
    x = 0
    y = 1
    for i in range(0,n):
        x , y = y, x + y
        fib.append(y)
        i = i + 1
    return fib

#(5)
def polar_cart(r,theta):
    return('x=', r*cos(theta), 'y=',r*sin(theta))
    
#(6)
def cart_polar(x,y):
    r = sqrt(x**2 + y**2)
    if x != 0:
        theta = atan(y/x)
    else:
        if y < 0:
            theta = 3*pi/2
        else:
            if y > 0:
                theta = pi/2
            else:
                if y == 0:
                    r, theta = 0, 0
    if x < 0:
        theta = atan(y/x) + pi
    if x > 0 and y < 0:
        theta = 2*pi + atan(y/x)
        
    return(r, theta)

# 5B
#(1)
def x_to_n(x,n):
    return x**n

def eval_poly(x, coeffs):
    a = 0
    for i in range(len(coeffs)):
        a = a + coeffs[i]*x_to_n(x,i)
    return print('P(',x,')=',a) 

#(2)
eval_poly(6,[2,3,0,1])
eval_poly(sqrt(2),[2,0,-1])
# 236 is an accuate value for P_1(6), however -4.4e-16 is not accurate for P_2(sqrt(2)) (since you should get zero). 
#This is because python stores sqrt(2) as a floating point number as this is the closest python can get to the decimal value of sqrt(2).

#(3)
def horner(x,coeffs):
    coeffs.reverse()
    b = 0
    for a in coeffs:
        b = a + x*b
    return print('P(',x,')=',b)

def horner_dif(x,coeffs):
    coeffs.reverse()
    b = 0
    c = 0
    for i in range(0, len(coeffs) -1):
            b = coeffs[i] + x*b
            c = b + x*c
    return print('P`(',x,')=',c)

#(4)
#a
horner(1,[0,0,1,-4,0,7])
horner_dif(1,[0,0,1,-4,0,7])

#b
horner(pi,[0,0,1,-4,0,7])
horner_dif(pi,[0,0,1,-4,0,7])

#(5)
horner(pi/4,[0,1,0,-1/6,0,1/120,0,-1/5040]) #-1/6,1/120 and -1/5040 are -1/3!,1/5! and -1/7! respectively.