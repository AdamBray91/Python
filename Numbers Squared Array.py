def Numbers_Squared2(a):
    i=1
    numbers = []
    while i <= a:
        numbers.append((i,i**2))
        i += 1
        if i**2 > 200:
            break
    print(numbers)
Numbers_Squared2(5)