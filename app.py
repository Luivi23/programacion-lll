import tkinter as tk
from tkinter import ttk, messagebox
import db

def agregar_producto():
    nombre = entry_nombre.get()
    precio = entry_precio.get()
    if nombre == "" or precio == "":
        messagebox.showwarning("Advertencia", "Todos los campos son obligatorios")
        return
    try:
        db.agregar_producto(nombre, precio)
        messagebox.showinfo("Éxito", "Producto agregado correctamente")
        entry_nombre.delete(0, tk.END)
        entry_precio.delete(0, tk.END)
        mostrar_productos()
    except Exception as e:
        messagebox.showerror("Error", str(e))

def eliminar_producto():
    selected_item = tree.focus()
    if not selected_item:
        messagebox.showwarning("Advertencia", "Seleccione un producto")
        return
    item_data = tree.item(selected_item)
    id_producto = item_data['values'][0]
    db.eliminar_producto(id_producto)
    messagebox.showinfo("Éxito", "Producto eliminado correctamente")
    mostrar_productos()

def mostrar_productos():
    for row in tree.get_children():
        tree.delete(row)
    for producto in db.obtener_productos():
        tree.insert("", tk.END, values=producto)

# Interfaz
root = tk.Tk()
root.title("Gestión de Productos")
root.geometry("400x400")

# Campos
ttk.Label(root, text="Nombre:").pack(pady=5)
entry_nombre = ttk.Entry(root)
entry_nombre.pack(pady=5)

ttk.Label(root, text="Precio:").pack(pady=5)
entry_precio = ttk.Entry(root)
entry_precio.pack(pady=5)

# Botones
ttk.Button(root, text="Agregar Producto", command=agregar_producto).pack(pady=5)
ttk.Button(root, text="Eliminar Producto", command=eliminar_producto).pack(pady=5)

# Tabla
columns = ("ID", "Nombre", "Precio")
tree = ttk.Treeview(root, columns=columns, show="headings")
for col in columns:
    tree.heading(col, text=col)
tree.pack(expand=True, fill=tk.BOTH, pady=10)

# Cargar productos al iniciar
mostrar_productos()

root.mainloop()
