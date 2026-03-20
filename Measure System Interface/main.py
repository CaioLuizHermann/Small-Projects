import tkinter as tk
import convert
window = tk.Tk()
window.title("Conversor de Unidades")
window.geometry("400x300")

text = tk.Label(window, text="\nWelcome!\n Select one of the units bellow using only numbers: \n <1> Cm \n <2> M \n <3> Km \n <4> End Program \n")
text.pack()

entry_unit = tk.Entry(window)
entry_unit.pack()
entry_value = tk.Entry(window)
entry_value.pack()
entry_final_unit = tk.Entry(window)
entry_final_unit.pack()
text_result = tk.Label(window)
def calculate():
    first_unit = entry_unit.get()
    quantity = entry_value.get()
    final_unit = entry_final_unit.get()
    try:
        first_unit = int(first_unit)
        quantity = float(quantity)
        final_unit = int(final_unit)
        meters = convert.convert_to_meters(first_unit, quantity)
        result = convert.convert_from_meters(meters, final_unit)
        result = float(result)
        text_result.config(window, text="The result is... " + str(result))
    except ValueError:
        error = tk.Label(text="Error: Invalid number.")
    except tk.TclError:
        error = tk.Label(text="Error")

calculate_button = tk.Button(window, text="convert", command=calculate)
calculate_button.pack()
text_result.pack()
window.mainloop()