import sqlite3
from reportes.reporte_base import FilaReporte
class ReporteRepositorio:
    def __init__(self):
        self.conexion = sqlite3.connect('./estadisticas.db')

    def obtenerTablaDeFrecuenciasPorCurso(self, id_curso):
        c = self.conexion.cursor()
        c.execute("SELECT nota as 'x', count(nota) as 'f' FROM examenes WHERE id_curso = ? GROUP BY nota ORDER BY nota ASC", (id_curso,))
        filas = c.fetchall()
        self.conexion.close()
        tabla = []
        for fila in filas:
            tabla.append(FilaReporte(fila[0], fila[1]))
        return tabla
