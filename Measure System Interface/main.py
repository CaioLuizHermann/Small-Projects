import tkinter as tk
import convert
window = tk.Tk()
window.title("Conversor de Unidades")
window.geometry("1100x900")
def clean_entry_unit(event):
    if entry_unit.get() == "First Unit, Ex: 1":
        entry_unit.delete(0, tk.END)
        entry_unit.config(fg="black")
def reset_entry_unit(event):
    if entry_unit.get() == "":
        entry_unit.insert(0, "First Unit, Ex: 1")
        entry_unit.config(fg="gray")
def clean_entry_value(event):
    if entry_value.get() == "Quantity, Ex: 100":
        entry_value.delete(0, tk.END)
        entry_value.config(fg="black")
def reset_entry_value(event):
    if entry_value.get() == "":
        entry_value.insert(0, "Quantity, Ex: 100")
        entry_value.config(fg="gray")
def clean_entry_final_unit(event):
    if entry_final_unit.get() == "Final Unit, Ex: 2":
        entry_final_unit.delete(0, tk.END)
        entry_final_unit.config(fg="black")
def reset_entry_final_unit(event):
    if entry_final_unit.get() == "":
        entry_final_unit.insert(0, "Final Unit, Ex: 2")
        entry_final_unit.config(fg="gray")

text1 = tk.Label(window, text="\nWelcome!\n Select one of the units bellow using only numbers: \n <1> Cm \n <2> M \n <3> Km \n", font=("Arial", 20))
text1.pack()

entry_unit = tk.Entry(window, width=40, font=("Arial", 16), bg="lightgray")
entry_unit.insert(0, "First Unit, Ex: 1")
entry_unit.config(fg="gray")
entry_unit.pack()
entry_unit.bind("<FocusIn>", clean_entry_unit)
entry_unit.bind("<FocusOut>", reset_entry_unit)
entry_value = tk.Entry(window,width=40, font=("Arial", 16), bg="lightgray")
entry_value.insert(0, "Quantity, Ex: 100")
entry_value.config(fg="gray")
text_value = tk.Label(window, text="\n Now, in the box bellow, insert the quantity you want to convert \n", font=("Arial", 20))
text_value.pack()
entry_value.pack()
entry_value.bind("<FocusIn>", clean_entry_value)
entry_value.bind("<FocusOut>", reset_entry_value)
entry_final_unit = tk.Entry(window, width=40, font=("Arial", 16), bg="lightgray")
entry_final_unit.insert(0, "Final Unit, Ex: 2")
entry_final_unit.config(fg= "gray")
entry_final_unit.bind("<FocusIn>", clean_entry_final_unit)
entry_final_unit.bind("<FocusOut>", reset_entry_final_unit)
text_final_unit = tk.Label(window, text="\n Finally, insert the number of the unit you want to convert to using the numbers bellow: \n <1> Cm \n <2> M \n <3> Km \n", font=("Arial", 20))
text_final_unit.pack()
entry_final_unit.pack()
text_spacement = tk.Label(window, text="\n", font=("Arial", 10))
text_spacement.pack()
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
        text_result.config(text="The result is... " + str(result), font=("Arial", 16))
    except ValueError:
        error = tk.Label(text="Error: Invalid number.", font=("Arial", 14))
        error.pack()
    except tk.TclError:
        error = tk.Label(text="Error", font=("Arial", 14))
        error.pack()

calculate_button = tk.Button(window, text="convert", command=calculate, width=50, height=1, font=("Arial", 20), bg="lightgray")
calculate_button.pack()
text_result.pack()
window.mainloop()