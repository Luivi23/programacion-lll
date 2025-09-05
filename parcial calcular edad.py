import tkinter as tk
from datetime import date

def calcular_edad():
    try:
        # obtener datos
        dia = int(entry_dia.get())
        mes = int(entry_mes.get())
        anio = int(entry_anio.get())

        hoy = date.today()
        nacimiento = date(anio, mes, dia)

        edad = hoy.year - nacimiento.year
        # Ajustar si aún no ha cumplido años este año
        if (hoy.month, hoy.day) < (nacimiento.month, nacimiento.day):
            edad -= 1

        lbl_resultado.config(text=f"Tienes {edad} años.")
    except ValueError:
        lbl_resultado.config(text=" ingresa una fecha válida.")

#  principal
ventana = tk.Tk()
ventana.title("Calculadora de Edad")
ventana.geometry("300x250")

# pedir fecha de nacimiento
tk.Label(ventana, text="Día de nacimiento:").pack()
entry_dia = tk.Entry(ventana)
entry_dia.pack()

tk.Label(ventana, text="Mes de nacimiento:").pack()
entry_mes = tk.Entry(ventana)
entry_mes.pack()

tk.Label(ventana, text="Año de nacimiento:").pack()
entry_anio = tk.Entry(ventana)
entry_anio.pack()

# calcular
tk.Button(ventana, text="Calcular tu Edad", command=calcular_edad).pack(pady=20)

# mostrar resultado
lbl_resultado = tk.Label(ventana, text="", font=("Arial", 12, "bold"))
lbl_resultado.pack(pady=10)

ventana.mainloop()
