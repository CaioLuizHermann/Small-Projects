import tkinter as tk
import customtkinter
from PIL import Image
from pathlib import Path
import convert

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")
app = customtkinter.CTk()
app.title("Ctk Test")
BASE_DIR = Path(__file__).resolve().parent
image_path = BASE_DIR / "squirtle.png"
image_org_squirtle = Image.open(image_path)
image = customtkinter.CTkImage(
    dark_image=image_org_squirtle,
    size=(300, 300)
)
label_img = customtkinter.CTkLabel(master=app, image=image, text="")
label_img.place(relx=1.1, rely=1.0, anchor="se", x=-10, y=-10)
def resize_img(event):
    width = app.winfo_width()
    new_size = (width // 3, width // 3)
    new_image = customtkinter.CTkImage(
        dark_image=image_org_squirtle,
        size=new_size
    )
    label_img.configure(image=new_image)
    label_img.image = new_image
app.bind("<Configure>", resize_img)
app.geometry("900x900")
float_offset = 0
direction = 1
def animate_squirtle():
    global float_offset,direction

    float_offset += direction

    if float_offset >= 15:
        direction = -1
    elif float_offset <= 0:
        direction = 1

    label_img.place(
        relx=1.1,
        rely=1.0,
        anchor ="se",
        x=-10,
        y=-10 - float_offset
    )
    app.after(80, animate_squirtle)
animate_squirtle()
button1 = customtkinter.CTkButton(master=app, text="Next")
text1 = customtkinter.CTkLabel(master=app, text="\nWelcome!\n Select one of the units bellow using only numbers: \n   <1> Cm \n <2> M \n   <3> Km \n", font=("Arial", 20))
entry_unit = customtkinter.CTkEntry(master=app, width=200, font=("Arial", 16))
entry_unit_get = 0
entry_value = customtkinter.CTkEntry(master=app, width=200, font=("Arial", 16))
entry_value_get = 0
entry_final_unit = customtkinter.CTkEntry(master=app, width=200, font=("Arial", 16))
entry_final_unit_get = 0
def end_function():
    app.destroy()
button_end = customtkinter.CTkButton(master=app, text="End Program", font=("Arial", 20), command= end_function)
button_end.place(relx=0.5, rely=0.8, anchor=tk.CENTER)
def entry_unit_preparation():  
    text1.place(relx=0.5, rely=0.1, anchor=tk.CENTER)
    entry_unit.place(relx=0.5, rely=0.2, anchor=tk.CENTER)
    button1.place(relx=0.5, rely=0.3, anchor=tk.CENTER)
entry_unit_preparation()
def entry_value_preparation():
        try:
            global entry_unit_get
            entry_unit_get = int(entry_unit.get())
            if entry_unit_get > 0 and entry_unit_get < 4:
                text1.configure(text="Great! Now, insert the value you want to convert")
                entry_unit.destroy()
                button1.configure(command=final_unit_preparation)
                entry_value.place(relx=0.5, rely=0.2, anchor=tk.CENTER)
        except ValueError:
            text1.configure(text="Select one of the units bellow using only numbers: \n<1> Cm \n <2> M \n   <3> Km\nPlease, insert a valid number")
def final_unit_preparation():
    try:
        global entry_value_get
        entry_value_get = float(entry_value.get())
        if entry_value_get > 0:
            text1.configure(text="Great! Now, select the unit you want to convert to: \n   <1> Cm \n <2> M \n   <3> Km\n")
            entry_value.destroy()
            button1.configure(command=calculate_result, text="Calculate")
            entry_final_unit.place(relx=0.5, rely=0.2, anchor=tk.CENTER)
        else:
            raise ValueError
    except ValueError:
        text1.configure(text="Insert the value you want to convert using only positive numbers greater than 0, please")
def calculate_result():
    try:
        global entry_final_unit_get
        entry_final_unit_get = int(entry_final_unit.get())
        if entry_final_unit_get == 1:
            final_unit_text = "Cm"
        elif entry_final_unit_get == 2:
            final_unit_text = "M" 
        elif entry_final_unit_get == 3:
            final_unit_text = "Km"
        meters = convert.convert_to_meters(entry_unit_get, entry_value_get)
        result = convert.convert_from_meters(meters, entry_final_unit_get)
        result = float(result)
        text1.configure(text=f"The result is {result} {final_unit_text}")
    except ValueError:
        text1.configure(text=f"Value Error\nInsert only real numbers between 1-3 \nValue inserted {entry_final_unit_get}")
button1.configure(command=entry_value_preparation)
app.mainloop()
