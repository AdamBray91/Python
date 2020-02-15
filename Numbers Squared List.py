def Numbers_Squared(a):
    for i in range(1, a+1):
        if i**2 < 200:
            print(i, i**2)
        else:
            break
            
#example            
Numbers_Squared(17)

