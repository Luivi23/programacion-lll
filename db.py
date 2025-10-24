import mysql.connector
from mysql.connector import Error

def conectar():
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="bd2"
        )
        return conexion
    except Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None

def agregar_producto(nombre, precio):
    conexion = conectar()
    if conexion:
        cursor = conexion.cursor()
        cursor.execute("INSERT INTO articulos (nombre, precio) VALUES (%s, %s)", (nombre, precio))
        conexion.commit()
        conexion.close()

def eliminar_producto(id_producto):
    conexion = conectar()
    if conexion:
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM articulos WHERE id = %s", (id_producto,))
        conexion.commit()
        conexion.close()

def obtener_productos():
    conexion = conectar()
    if conexion:
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM articulos")
        productos = cursor.fetchall()
        conexion.close()
        return productos
    return []
