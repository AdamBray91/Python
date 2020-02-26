#Ask the user for a number and determine whether the number is prime or not.

number = int(input("Enter a number to check if it is prime: "))
list = range(2,number+1)
divisors = [i for i in list if number%i == 0]
if len(divisors) > 1:
    print(number, "is not prime")
else:
    print(number, "is prime")
