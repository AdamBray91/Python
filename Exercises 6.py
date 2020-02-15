#Ask the user for a string and print out whether this string is a palindrome or not

string = str(input("Input a word: "))
if string[::-1] == string:
    print(string, "is a palendrome")
else:
    print(string, "is not a palendrome")

