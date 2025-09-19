import tkinter as tk

def calcular_promedio():
    try:
        # Obtener valores de las entradas
        nota1 = float(entry1.get())
        nota2 = float(entry2.get())
        nota3 = float(entry3.get())

        # Calcular promedio
        promedio = (nota1 * 0.30) + (nota2 * 0.30) + (nota3 * 0.40 )

        # Mostrar resultado en la etiqueta
        lbl_resultado.config(text=f"Su promedio es: {promedio:.2f}")
    except ValueError:
        lbl_resultado.config(text="Por favor ingrese solo números.")

# Crear ventana
ventana = tk.Tk()
ventana.title("Promedio de 3 Notas")
ventana.geometry("300x250")

# Etiquetas y entradas
tk.Label(ventana, text="lab 1 (30%) :").pack()
entry1 = tk.Entry(ventana)
entry1.pack()

tk.Label(ventana, text="lab 2 (30%) :").pack()
entry2 = tk.Entry(ventana)
entry2.pack()

tk.Label(ventana, text="parcial (40%) :").pack()
entry3 = tk.Entry(ventana)
entry3.pack()

# Botón para calcular
btn = tk.Button(ventana, text=" Promediar ", command=calcular_promedio)
btn.pack(pady=19)

# Etiqueta para mostrar resultado
lbl_resultado = tk.Label(ventana, text="", font=("Arial", 12, "bold"))
lbl_resultado.pack(pady=10)

ventana.mainloop()

