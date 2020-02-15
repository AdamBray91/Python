#Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user.
#Extras
#If the number is a multiple of 4, print out a different message.
#Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). If check divides evenly into num, tell that to the user. If not, print a different appropriate message.

number = int(input("Input a number:"))
if number%2 == 0:
    if number%4 == 0:
        print(number, "is divisible by 4")
    else:
        print(number, "is even")
else:
    print(number, "is odd")
    
num = int(input("Input first number:"))
check = int(input("Input second number:"))
if check%num ==0:
    print(check, "divides evenly into", num)
else:
    print(check, "does not divide evenly into", num)