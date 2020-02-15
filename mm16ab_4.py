# import files here
from math import floor, sqrt, pi, e

# 4A 
# function
def contfrac(a,i):
    cf=[]
    while i > 0:
        cf.append(floor(a))
        a = 1.0/(a-floor(a))
        i = i - 1
    return(cf)
    
# Answers to questions
print(contfrac(sqrt(2),20))
print(contfrac(sqrt(3),20))
print(contfrac(sqrt(7),20))
print(contfrac(pi,20))
print(contfrac(e,20))
print('If a_i = 0 for some i = {1,2,3,...}, then you can do 1 over the fraction to get a_i = a_(i+1).')

# 4B
# function
def contfrac2(num,den):
    cf=[]
    while den > 0:
        cf.append(num//den)
        num = num%den
        num, den = den, num 
    return(cf)
    
# Answers to questions
print(contfrac2(97,61))
print(contfrac2(1066,1012))
print(contfrac2(123456789,987654321))

#4C
# function
def partcon(a,k): 
    den = contfrac(a,20)[k-1]
    num = 1
    for j in range(2,k+1):
        num = contfrac(a,20)[k-j]*den + num
        num, den = den, num
    return(den, num)
    
#Answers to questions
print(partcon(sqrt(2),1)[0],'/',partcon(sqrt(2),1)[1])
print(partcon(sqrt(2),2)[0],'/',partcon(sqrt(2),2)[1])
print(partcon(sqrt(2),3)[0],'/',partcon(sqrt(2),3)[1])
print(partcon(sqrt(2),4)[0],'/',partcon(sqrt(2),4)[1])
print(partcon(sqrt(2),5)[0],'/',partcon(sqrt(2),5)[1])
print(partcon(sqrt(2),6)[0],'/',partcon(sqrt(2),6)[1])

print(partcon(pi,4)[0],'/',partcon(pi,4)[1])

print(partcon(sqrt(5),5)[0],'/',partcon(sqrt(5),5)[1])