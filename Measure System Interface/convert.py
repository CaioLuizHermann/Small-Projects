import tkinter as tk
def convert_to_meters(first_unit, quantity):
    if first_unit not in (1,2,3):
        raise ValueError
    if first_unit == 1:
        meters = quantity/100
    elif first_unit == 2:
        meters = quantity
    elif first_unit == 3:
        meters = quantity*1000
    return meters

def convert_from_meters(meters, final_unit):
    if final_unit not in (1,2,3):
        raise ValueError
    if final_unit == 1:
        result = meters*100
    elif final_unit == 2:
        result = meters
    elif final_unit == 3:
        result = meters/1000
    return result

