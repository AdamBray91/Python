def Numbers_Squared(a):
    i=1
    numbers = []
    while i <= a:
        numbers.append((i,i**2))
        i += 1
        if i**2 > 200:
            break
    print(numbers)

#example    
Numbers_Squared(15)
