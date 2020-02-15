#Take two lists and write a program that returns a list that contains only the elements that are common between the lists using comparison
import random

a = random.sample(range(100),random.randint(10,20))
b = random.sample(range(100),random.randint(10,20))
print([i for i in a if i in b])