#Create a program that asks the user for a number and then prints out a list of all the divisors of that number
number = int(input("Input a number to find divisors: "))
list = range(1,number+1)
divisors = []
for i in list:
    if number%i == 0:
        divisors.append(i)
print(divisors)
