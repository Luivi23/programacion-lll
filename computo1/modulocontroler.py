# This code is generated using PyUIbuilder: https://pyuibuilder.com


import os
import tkinter as tk
from tkinter import ttk

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

main = tk.Tk()
main.title("Main Window")
main.config(bg="#E4E2E2")
main.geometry("700x400")

style = ttk.Style(main)
style.theme_use("clam")


def cambiar_color():
    color = color_var.get()
    if color == "verde":
        main.config(bg="yellow")
    elif color == "azul":
        main.config(bg="violet")
    elif color == "rojo":
        main.config(bg="darkred")


style.configure("button2.TButton", background="#E4E2E2", foreground="#000")
style.map("button2.TButton", background=[("active", "#E4E2E2")], foreground=[("active", "#000")])

button2 = ttk.Button(master=main, text="Salir", style="button2.TButton", command=main.destroy)
button2.place(x=249, y=266, width=80, height=40)


style.configure("button1.TButton", background="#E4E2E2", foreground="#000")
style.map("button1.TButton", background=[("active", "#E4E2E2")], foreground=[("active", "#000")])

button1 = ttk.Button(master=main, text="Cambiar", style="button1.TButton", command=cambiar_color)
button1.place(x=250, y=182, width=80, height=40)


color_var = tk.StringVar(value="")

style.configure("TRadiobutton", background="#E4E2E2", foreground="#000")
style.map("TRadiobutton", background=[("active", "#E4E2E2")], foreground=[("active", "#000")])

buttomverde = ttk.Radiobutton(master=main, variable=color_var, text="amarillo", value="verde", style="TRadiobutton")
buttomverde.place(x=248, y=33)

buttonazul = ttk.Radiobutton(master=main, variable=color_var, text="morado", value="azul", style="TRadiobutton")
buttonazul.place(x=244, y=76)

buttonrojo = ttk.Radiobutton(master=main, variable=color_var, text="rojo", value="rojo", style="TRadiobutton")
buttonrojo.place(x=242, y=118)

main.mainloop()
