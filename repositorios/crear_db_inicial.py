import sqlite3

conn = sqlite3.connect('./estadisticas.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS alumnos (
             id INTEGER PRIMARY KEY,
             alias TEXT,
             email TEXT)''')