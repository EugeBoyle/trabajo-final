import sqlite3
from entidades.curso import Curso


class CursoRepositorio:
    def __init__(self):
        self.conexion = sqlite3.connect('./estadisticas.db')
    
    def buscarPorId(self, id):
        c = self.conexion.cursor()
        c.execute("SELECT * FROM cursos WHERE id = ?", (id))
        fila = c.fetchone()
        self.conexion.close()
        return Curso(fila[0], fila[1], fila[2])
    
    def buscarTodos(self):
        c = self.conexion.cursor()
        c.execute("SELECT * FROM cursos")
        filas = c.fetchall()
        self.conexion.close()
        cursos=[]
        for fila in filas:
            cursos.append(Curso(fila[0], fila[1], fila[2]))
        return cursos

    def guardar(self, curso):
        c = self.conexion.cursor()
        c.execute("INSERT INTO cursos (nombre, duracion) VALUES (?, ?)", (curso.nombre, curso.duracion))
        self.conexion.commit()
        self.conexion.close()
    
    def modificar(self, id, nuevoNombre, nuevaDuracion):
        c = self.conexion.cursor()
        c.execute("UPDATE cursos SET nombre=?, duracion=? WHERE id=?", (nuevoNombre, nuevaDuracion, id))
        self.conexion.commit()
        self.conexion.close()

    def eliminar(self, id):
        c = self.conexion.cursor()
        c.execute("DELETE FROM cursos WHERE id=?", (id))
        self.conexion.commit()
        self.conexion.close()