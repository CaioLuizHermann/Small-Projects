def input_first_measure_system():
    try:
        first_measure_system = int(input("Choose the first measure system \n <1> Cm \n <2> M \n <3> Km \n <4> End Program\n"))
    except ValueError:
        raise ValueError
    return first_measure_system
def input_quantity():
    try:
        quantity = float(input("Insert the quantity: \n"))
    except ValueError:
        raise ValueError
    return quantity
def input_second_measure_system():
    try:
        second_measure_system = int(input("Choose the second measure system \n <1> Cm \n <2> M \n <3> Km \n "))
    except ValueError:
        raise ValueError
    return second_measure_system