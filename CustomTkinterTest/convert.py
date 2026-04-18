def convert_to_meters(entry_unit_get, entry_value_get):
    if entry_unit_get not in (1,2,3):
        raise ValueError
    if entry_unit_get == 1:
        meters = entry_value_get/100
    elif entry_unit_get == 2:
        meters = entry_value_get
    elif entry_unit_get == 3:
        meters = entry_value_get*1000
    return meters

def convert_from_meters(meters, entry_final_unit_get):
    if entry_final_unit_get not in (1,2,3):
        raise ValueError
    if entry_final_unit_get == 1:
        result = meters*100
    elif entry_final_unit_get == 2:
        result = meters
    elif entry_final_unit_get == 3:
        result = meters/1000
    return result