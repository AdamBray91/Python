#Write a program (using functions!) that asks the user for a long string containing multiple words. 
#Print back to the user the same string, except with the words in backwards order.

sentence = input("Enter a sentence: ",)
def reverse_sentence(a):
    a = a.split()
    a.reverse()
    a = " ".join(a)
    return a
    
print(reverse_sentence(sentence))