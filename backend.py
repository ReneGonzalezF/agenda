import sqlite3



def crearTablaContactos():
    conexion=sqlite3.connect('base_de_datos.db')
    cursor=conexion.cursor()
    cursor.execute(''' CREATE TABLE IF NOT EXIST contactos
               (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                nombre TEXT, 
                telefono TEXT, 
                email TEXT)''')
    conexion.commit()
    conexion.close()

def agregarContactos (nombre,telefono,email):
    conexion=sqlite3.connect('base_de_datos.db')
    cursor=conexion.cursor()
    cursor.execute('''INSERT INTO contactos (nombre, telefono, email) VALUES (?,?,?)''',(nombre,telefono,email))
    conexion.commit()
    conexion.close()

def mostrarContactos():
    conexion=sqlite3.connect('base_de_datos.db')
    cursor=conexion.cursor()
    cursor.execute('''SELECT id,nombre, telefono, email FROM contactos''')
    contactos=cursor.fetchall()
    conexion.close()
    return contactos

def eliminarContactos(nombre):
    conexion=sqlite3.connect('base_de_datos.db')
    cursor=conexion.cursor()
    cursor.execute('DELETE  FROM contactos WHERE nombre = ?',(nombre,))
    conexion.commit()
    conexion.close()

def buscarContactos(nombre):
    conexion=sqlite3.connect('base_de_datos.db')
    cursor=conexion.cursor()
    cursor.execute('SELECT id, nombre, telefono, email  FROM contactos WHERE nombre = ?',(nombre,))
    contactos=cursor.fetchall()
    conexion.close()
    return contactos





