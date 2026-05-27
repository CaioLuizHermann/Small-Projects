# Import libraries and other things
import tkinter as tk
import customtkinter as ctk
from PIL import Image, ImageTk
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent
import converter_main as converter_program
# WIndow Configs
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")
main_app = ctk.CTk()
main_app.title("Main Page")
main_app.geometry("1200x900")
BASE_W = 1200
BASE_H = 900
canvas = ctk.CTkCanvas(main_app, width=1200, height=900)
img = Image.open(BASE_DIR / "pfp.png")
img_ref = None
canvas.pack(fill="both", expand=True)
convert_button = ctk.CTkButton(
    master=main_app,
    text="Metric Units Coverter",
    width=200,
    height=50,
    command= lambda: converter_program.converter(main_app),
    font=("Arial", 20))
convert_button.place(relx=0.9, rely=0.1, anchor="ne")
def configure_widgets(events=None):
    global img_ref
    width_app = main_app.winfo_width()
    height_app = main_app.winfo_height()
    if width_app < 2 or height_app < 2:
        return
    scalling = min(
        width_app / BASE_W,
        height_app / BASE_H
    )
    proportion_img = 0.3
    width_img = int(width_app * proportion_img)
    height_img = int((height_app * 1.3) * proportion_img)
    scalling = max(0.2, min(scalling, 2))
    new_img = img.resize(
        (width_img,height_img)
    )
    height_convert_button = int(50 * scalling)
    width_convert_button = int(200* scalling)
    font_convert_button = int(20* scalling)

    convert_button.configure(
        width=width_convert_button,
        height=height_convert_button,
        font=("Arial", font_convert_button)
    )
    img_ref =ImageTk.PhotoImage(new_img)
    canvas.delete("all")
    canvas.create_image(0, 0, anchor="nw", image=img_ref)
main_app.bind("<Configure>", configure_widgets)
configure_widgets()
main_app.mainloop()