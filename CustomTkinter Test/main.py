import tkinter as tk 
import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")
button1_counter = 0
app = customtkinter.CTk()
app.title("Ctk Test")
app.geometry("1100x900")
button1 = customtkinter.CTkButton(master=app, text="Next")
text1 = customtkinter.CTkLabel(master=app, text="\nWelcome!\n Select one of the units bellow using only numbers: \n   <1> Cm \n <2> M \n   <3> Km \n", font=("Arial", 20))
entry_unit = customtkinter.CTkEntry(master=app, width=200, font=("Arial", 16))
def entry_unit_preparation():  
    text1.place(relx=0.5, rely=0.1, anchor=tk.CENTER)
    entry_unit.place(relx=0.5, rely=0.2, anchor=tk.CENTER)
    button1.place(relx=0.5, rely=0.3, anchor=tk.CENTER)
entry_unit_preparation()
def entry_value_preparation():
    button1_counter == button1_counter + 1
    if button1_counter == 1:
        text1.destroy()
        entry_unit.destroy()
        button1.destroy()
button1.configure(command=entry_value_preparation)
text2 = customtkinter.CTkLabel(master=app, text="\nGreat! Now, insert the unit you want to convert", font=("Arial", 20))
btn = customtkinter.CTkButton(master=app, text="Cool Button")
btn.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
app.mainloop()
