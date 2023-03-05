import sqlite3
from entidades.examen import Examen


class ExamenRepositorio:
    def __init__(self):
        self.conexion = sqlite3.connect('./estadisticas.db')
    
    def buscarPorId(self, id):
        c = self.conexion.cursor()
        c.execute("SELECT * FROM examenes WHERE id = ?", (id))
        fila = c.fetchone()
        self.conexion.close()
        return Examen(fila[0], fila[1], fila[2])
    
    def buscarTodos(self):
        c = self.conexion.cursor()
        c.execute("SELECT * FROM examenes")
        filas = c.fetchall()
        self.conexion.close()
        examenes=[]
        for fila in filas:
            examenes.append(Examen(fila[0], fila[1], fila[2]))
        return examenes

    def guardar(self, examen):
        c = self.conexion.cursor()
        c.execute("INSERT INTO examenes (nota, id_curso, id_alumno) VALUES (?, ?, ?)", (examen.nota, examen.id_curso, examen.id_alumno))
        self.conexion.commit()
        self.conexion.close()