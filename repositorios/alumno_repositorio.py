import sqlite3
from entidades.alumno import Alumno

class AlumnoRepositorio:
    def __init__(self):
        self.conexion = sqlite3.connect('./estadisticas.db')
    
    def buscarPorId(self, id):
        c = self.conexion.cursor()
        c.execute("SELECT * FROM alumnos WHERE id = ?", (id))
        fila = c.fetchone()
        self.conexion.close()
        return Alumno(fila[0], fila[1], fila[2])
    
    def buscarTodos(self):
        c = self.conexion.cursor()
        c.execute("SELECT * FROM alumnos")
        filas = c.fetchall()
        self.conexion.close()
        alumnos=[]
        for fila in filas:
            alumnos.append(Alumno(fila[0], fila[1], fila[2]))
        return alumnos

    def guardar(self, alumno):
        c = self.conexion.cursor()
        c.execute("INSERT INTO alumnos (alias, email) VALUES (?, ?)", (alumno.alias, alumno.email))
        self.conexion.commit()
        self.conexion.close()
    
    def modificar(self, id, nuevoAlias, nuevoEmail):
        c = self.conexion.cursor()
        c.execute("UPDATE alumnos SET alias=?, email=? WHERE id=?", (nuevoAlias, nuevoEmail, id))
        self.conexion.commit()
        self.conexion.close()

    def eliminar(self, id):
        c = self.conexion.cursor()
        c.execute("DELETE FROM alumnos WHERE id=?", (id))
        self.conexion.commit()
        self.conexion.close()