import tkinter as tk
import input_utils
end = False
window = tk.Tk()
window.title("Conversor de Unidades")
window.geometry("400x300")
while not end:
    text = tk.Label(window, text="\nWelcome!\n Select one of the units bellow using only numbers: \n <1> Cm \n <2> M \n <3> Km \n <4> End Program \n")
    text.pack()
    
    window.mainloop()