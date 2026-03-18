end = False
while end == False:
    result = 0
    meters = 0
    
    try:
        m1 = float(input("Insert the quantity: \n"))
    except:
        print("Error 0: Invalid Number \n")
        continue
    if c1 == 1:
        meters = m1/100
    elif c1 == 2:
        meters = m1
    elif c1 == 3:
        meters = m1*1000
    try:
        c2 = int(input("Choose the second measure system \n <1> Cm \n <2> M \n <3> Km \n "))
    except:
        print("Error 0: Invalid Number")
        continue
    if c2 == 1: 
        result = meters*100
    elif c2 == 2:
        result = meters
    elif c2 == 3:
        result = meters/1000
    elif c2 > 3 or c2 < 1:
        print("Error 0: \n Invalid number")
        continue
    print("The result is... \n ", result, "\n \n" )
