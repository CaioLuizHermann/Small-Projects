import tkinter as tk
import input_utils
import convert
end = False
window = tk.Tk()
window.title("Conversor de Unidades")
window.geometry("400x300")
try:
    text = tk.Label(window, text="\nWelcome!\n Select one of the units bellow using only numbers: \n <1> Cm \n <2> M \n <3> Km \n <4> End Program \n")
    text.pack()
    first_unit = input_utils.entry_measure_unit(window)
    if first_unit == 4:
        print("Exiting Prograsm...")
        end = True 
        window.quit()
       
    quantity = input_utils.entry_quantity(window)
    meters = convert.convert_to_meters(first_unit,quantity)
    final_unit = input_utils.entry_final_unit(meters, final_unit)
    result = convert.convert_from_meters()
    result_text = tk.Label(window, result_text=("\n The result is.... \n", result)
    window
except ValueError:
    error_text = tk.Label(window, text="Error 0: Invalid value")
    error_text.pack()
