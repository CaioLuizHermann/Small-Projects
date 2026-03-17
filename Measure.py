end = False
while end == False:
    first_value = 0
    value = 0
    result = 0
    c1 = int(input("Choose the first measure system \n <1> Cm \n <2> M \n <3> Km \n <4> End Program\n"))
    if c1 == 1:
        m1 = float(input("Insert the quantity: \n"))
        first_value = 1
    elif c1 == 2:
        m1 = float(input("Insert the quantity: \n"))
        first_value = 2
    elif c1 == 3:
        m1 = float(input("Insert the quantity: \n"))
        first_value = 3
    elif c1 == 4:
        end = True
    elif c1 >= 5 or c1 <= 0:
        print("Error 0: \n Invalid number\n")
    if end == False:
        c2 = int(input("Choose the second measure system \n <1> Cm \n <2> M \n <3> Km \n "))
        if c2 == 1:
            if first_value == 1:
                result = m1
            if first_value == 2:
                result = m1/100
            if first_value == 3:
                result = m1/100000
        elif c2 == 2:
            if first_value == 1:
                result = m1*100
            if first_value == 2:
                result = m1
            if first_value == 3:
                result = m1/1000
        elif c2 == 3:
            if first_value == 1:
                result = m1/100000
            if first_value == 2:
                result = m1/1000
            if first_value == 3:
                result = m1
        elif c2 >= 4 or c2 <= 0:
            print("Error 0: \n Invalid number")
            print("The result is... \n ", result )
