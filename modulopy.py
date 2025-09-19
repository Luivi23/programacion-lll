# This code is generated using PyUIbuilder: https://pyuibuilder.com

import tkinter as tk
from tkinter import ttk

class Aplicacion:
    def __init__(self, ventana):
        self.valor = 0
        self.ventana = ventana
        self.ventana.title("Controles con ttk")
        self.ventana.config(bg="#E4E2E2")
        self.ventana.geometry("700x400")

        style = ttk.Style(self.ventana)
        style.theme_use("clam")

        # Label
        style.configure("label1.TLabel", background="#E4E2E2", foreground="#000")
        self.label1 = ttk.Label(master=self.ventana, text=str(self.valor), style="label1.TLabel")
        self.label1.place(x=241, y=145, width=80, height=40)


        style.configure("button1.TButton", background="#E4E2E2", foreground="#000")
        style.map("button1.TButton", background=[("active", "#E4E2E2")], foreground=[("active", "#000")])
        self.button1 = ttk.Button(master=self.ventana, text="aumentar", style="button1.TButton", command=self.aumenta)
        self.button1.place(x=244, y=199, width=80, height=40)

        #
        style.configure("button2.TButton", background="#E4E2E2", foreground="#000")
        style.map("button2.TButton", background=[("active", "#E4E2E2")], foreground=[("active", "#000")])
        self.button2 = ttk.Button(master=self.ventana, text="disminuir", style="button2.TButton", command=self.disminuir)
        self.button2.place(x=246, y=255, width=80, height=40)

        # Botón salir
        style.configure("button3.TButton", background="#E4E2E2", foreground="#000")
        style.map("button3.TButton", background=[("active", "#E4E2E2")], foreground=[("active", "#000")])
        self.button3 = ttk.Button(master=self.ventana, text="salir", style="button3.TButton", command=self.ventana.quit)
        self.button3.place(x=592, y=311, width=80, height=40)

    def aumenta(self):
        self.valor += 1
        self.label1.config(text=str(self.valor))

    def disminuir(self):
        self.valor -= 1
        self.label1.config(text=str(self.valor))


if __name__ == "__main__":
    ventana = tk.Tk()
    app = Aplicacion(ventana)
    ventana.mainloop()
