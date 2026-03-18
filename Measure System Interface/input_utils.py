import tkinter as tk
def entry_measure_unit(window):
        first_unit = tk.Entry(window, width=20)
        return first_unit
def entry_quantity(window):
        quantity = tk.Entry(window, width=20)
        return quantity
def entry_final_unit(window):
        final_unit = tk.Entry(window, width=20)
        return final_unit
def entry_grab(first_unit, quantity, final_unit):
        first_unit_value = int(first_unit.get())
        quantity_value = float(quantity.get())
        final_unit_value = int(final_unit.get())
        return first_unit_value, quantity_value, final_unit_value