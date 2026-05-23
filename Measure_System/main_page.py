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
canvas = tk.Canvas(main_app, highlightthickness=0, bg="#EBEBEB")
canvas.place(relwidth=1, relheight=1)
main_app.geometry("1200x900")
BASE_W = 1200
BASE_H = 900

convert_button = ctk.CTkButton(
    master=main_app,
    text="Metric Units Coverter",
    width=200,
    height=50,
    command= lambda: converter_program.converter(main_app),
    font=("Arial", 20))

convert_button.pack(expand=True)
convert_button.place(relx=0.9, rely=0.1, anchor="ne")
def configure_widgets(events=None):
    width_app = main_app.winfo_width()
    height_app = main_app.winfo_height()

    scalling = min(
        width_app / BASE_W,
        height_app / BASE_H
    )

    scalling = max(0.2, min(scalling, 2))

    width_convert_button = int(200* scalling)
    height_convert_button = int(50 * scalling),
    font_convert_button = int(20* scalling)

    convert_button.configure(
        width=width_convert_button,
        height=height_convert_button,
        font=("Arial", font_convert_button)
    )
main_app.bind("<Configure>", configure_widgets)
configure_widgets()
main_app.mainloop()