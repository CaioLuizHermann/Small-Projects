def convert_to_meters(quantity,first_measure_system):
    if first_measure_system not in (1,2,3):
        raise ValueError
    if first_measure_system == 1:
        meters = quantity/100
    elif first_measure_system == 2:
        meters = quantity
    elif first_measure_system == 3:
        meters = quantity*1000
    return meters
def convert_from_meters(meters, second_measure_system):
    if second_measure_system not in (1,2,3):
        raise ValueError
    if second_measure_system == 1: 
        result = meters*100
    elif second_measure_system == 2:
        result = meters
    elif second_measure_system == 3:
        result = meters/1000
    return result