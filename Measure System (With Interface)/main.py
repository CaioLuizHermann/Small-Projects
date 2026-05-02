# Import libraries
import tkinter as tk
import customtkinter
from PIL import Image, ImageTk
from pathlib import Path
import convert

# Window Configs
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")
app = customtkinter.CTk()
app.title("Ctk Test")
canvas = tk.Canvas(app, highlightthickness=0, bg="#242424")
canvas.place(relwidth=1, relheight=1)
app.geometry("900x900")
float_offset = 0
direction = 1
BASE_DIR = Path(__file__).resolve().parent

# Banner Image

image_path_banner = BASE_DIR / "banner.png"

image_org_banner = Image.open(image_path_banner)

image_red_banner = image_org_banner.resize((200, 900))

banner_img = ImageTk.PhotoImage(image_red_banner)

banner_id = canvas.create_image(900, 0, image=banner_img, anchor="ne")

# Squirtle Image

image_path = BASE_DIR / "squirtle.png"
image_org_squirtle = Image.open(image_path).convert("RGBA")
squirtle_tk = ImageTk.PhotoImage(image_org_squirtle.resize((300,300), Image.LANCZOS))
squirtle_id = canvas.create_image(0, 0, image=squirtle_tk, anchor="se")
def resize_img_squirtle(event):
    global squirtle_tk_ref
    size = app.winfo_width() // 3
    resized = image_org_squirtle.resize((size, size,), Image.LANCZOS)
    squirtle_tk_ref = ImageTk.PhotoImage(resized)
    canvas.itemconfig(squirtle_id, image=squirtle_tk_ref)


# Squirtle Animation

def animate_squirtle():
    global float_offset, direction

    float_offset += direction

    if float_offset >= 15:
        direction = -1
    elif float_offset <= 0:
        direction = 1

    w = app.winfo_width()
    h = app.winfo_height()
    canvas.coords(squirtle_id, w + 50, h - 10 - float_offset)
    app.after(80, animate_squirtle)
animate_squirtle()

# Resize All

def resize_all(event):
    resize_img_squirtle(event)
    resize_banner(event)
app.bind("<Configure>", resize_all)




# Resize Banner

def resize_banner(event):
        height = app.winfo_height()

        new_banner = image_org_banner.resize((200, height))

        global banner_img
        banner_img = ImageTk.PhotoImage(new_banner)

        canvas.itemconfig(banner_id, image = banner_img)
        canvas.coords(banner_id,app.winfo_width(), 0)


button1 = customtkinter.CTkButton(master=app, text="Next")
text1 = customtkinter.CTkLabel(master=app, text="\nWelcome!\n Select one of the units bellow using only numbers: \n   <1> Cm \n <2> M \n   <3> Km \n", font=("Arial", 20))
entry_unit = customtkinter.CTkEntry(master=app, width=200, font=("Arial", 16))
entry_unit_get = 0
entry_value = customtkinter.CTkEntry(master=app, width=200, font=("Arial", 16))
entry_value_get = 0
entry_final_unit = customtkinter.CTkEntry(master=app, width=200, font=("Arial", 16))
entry_final_unit_get = 0

# Functions 

def end_function():
    app.destroy()
button_end = customtkinter.CTkButton(master=app, text="End Program", command= end_function)
button_end.place(relx=0.5, rely=0.4, anchor=tk.CENTER)
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
def entry_unit_preparation():  
    text1.place(relx=0.5, rely=0.1, anchor=tk.CENTER)
    entry_unit.place(relx=0.5, rely=0.2, anchor=tk.CENTER)
    button1.place(relx=0.5, rely=0.3, anchor=tk.CENTER) 
    button1.configure(command=entry_value_preparation)
entry_unit_preparation()
def final_unit_preparation():
    try:
        global entry_value_get
        entry_value_get = float(entry_value.get())
        if entry_value_get <= 0:
            raise ValueError
        text1.configure(text="Great! Now, select the unit you want to convert to: \n   <1> Cm \n <2> M \n   <3> Km\n")
        entry_value.destroy()
        button1.configure(command=calculate_result, text="Calculate")
        entry_final_unit.place(relx=0.5, rely=0.2, anchor=tk.CENTER)
    except ValueError:
        text1.configure(text="Insert the value you want to convert using only positive numbers greater than 0, please")
def calculate_result():
    try:
        global entry_final_unit_get
        entry_final_unit_get = int(entry_final_unit.get())
        unit_names = {1: "Cm", 2: "M", 3: "Km"}
        if entry_final_unit_get not in unit_names:
            raise ValueError
        final_unit_text = unit_names[entry_final_unit_get]
        meters = convert.convert_to_meters(entry_unit_get, entry_value_get)
        result = convert.convert_from_meters(meters, entry_final_unit_get)
        result = float(result)
        text1.configure(text=f"The result is {result} {final_unit_text}")
    except ValueError:
        text1.configure(text=f"Value Error\nInsert only real numbers between 1-3 \nValue inserted {entry_final_unit_get}")

# Window Loop

app.mainloop()

