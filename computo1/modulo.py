import tkinter as tk
from tkinter import  ttk

class aplicacion:
    def __init__(self):
        self.valor=1
        self.ventana1=tk.Tk
        self.ventana1.title("controles con ttk")
        self.label1=ttk.label(self.ventana1, text=self.valor)
        self.label1.grid(colum=0, row=0)
        self.label1.configure(forground="red")

        self.boton1=ttk.Button(self.ventana1, text="aumentar", command=self.aumenta)
        self.boton1.grid(column=0, row=1)

        self.boton2=ttk.Button(self.ventana1, text="disminuir", command=self.disminuir)
        self.boton2.grid(column=0, row=2)

        self.ventana1.mainloop()


