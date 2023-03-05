import sqlite3

conn = sqlite3.connect('./estadisticas.db')
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS alumnos (
             id INTEGER PRIMARY KEY,
             alias TEXT,
             email TEXT)''')


c.execute('''CREATE TABLE IF NOT EXISTS cursos (
             id INTEGER PRIMARY KEY,
             nombre TEXT,
             duracion TEXT)''')

c.execute('''CREATE TABLE IF NOT EXISTS examenes (
             id INTEGER PRIMARY KEY,
             nota REAL,
             id_curso INTEGER,
             id_alumno INTEGER)''')
correrDataInicial = True
if correrDataInicial == True:
    c.execute("INSERT INTO alumnos (id, alias, email) VALUES (?, ?, ?)", (1,"jose", "jose@gmail.com"))
    c.execute("INSERT INTO alumnos (id, alias, email) VALUES (?, ?, ?)", (2,"pepe", "pepe@gmail.com"))
    c.execute("INSERT INTO alumnos (id, alias, email) VALUES (?, ?, ?)", (3,"carlos", "carlos@gmail.com"))
    c.execute("INSERT INTO alumnos (id, alias, email) VALUES (?, ?, ?)", (4,"franco", "franco@gmail.com"))
    c.execute("INSERT INTO alumnos (id, alias, email) VALUES (?, ?, ?)", (5,"mario", "mario@gmail.com"))
    c.execute("INSERT INTO alumnos (id, alias, email) VALUES (?, ?, ?)", (6,"ruben", "ruben@gmail.com"))
    c.execute("INSERT INTO alumnos (id, alias, email) VALUES (?, ?, ?)", (7,"laura", "laura@gmail.com"))
    c.execute("INSERT INTO alumnos (id, alias, email) VALUES (?, ?, ?)", (8,"maria", "maria@gmail.com"))
    c.execute("INSERT INTO alumnos (id, alias, email) VALUES (?, ?, ?)", (9,"carmen", "carmen@gmail.com"))
    c.execute("INSERT INTO alumnos (id, alias, email) VALUES (?, ?, ?)", (10,"miranda", "miranda@gmail.com"))

    c.execute("INSERT INTO cursos (id, nombre, duracion) VALUES (?, ?, ?)", (1, "python avanzado", 7))
    c.execute("INSERT INTO cursos (id, nombre, duracion) VALUES (?, ?, ?)", (2, "python para principiantes", 5))

    c.execute("INSERT INTO examenes (nota, id_curso, id_alumno) VALUES (?, ?, ?)", (6.5, 1, 1))
    c.execute("INSERT INTO examenes (nota, id_curso, id_alumno) VALUES (?, ?, ?)", (7, 1, 2))
    c.execute("INSERT INTO examenes (nota, id_curso, id_alumno) VALUES (?, ?, ?)", (6, 1, 3))
    c.execute("INSERT INTO examenes (nota, id_curso, id_alumno) VALUES (?, ?, ?)", (8, 1, 4))
    c.execute("INSERT INTO examenes (nota, id_curso, id_alumno) VALUES (?, ?, ?)", (9, 1, 5))
    c.execute("INSERT INTO examenes (nota, id_curso, id_alumno) VALUES (?, ?, ?)", (7, 1, 6))
    c.execute("INSERT INTO examenes (nota, id_curso, id_alumno) VALUES (?, ?, ?)", (7, 1, 7))
    c.execute("INSERT INTO examenes (nota, id_curso, id_alumno) VALUES (?, ?, ?)", (6, 1, 8))
    c.execute("INSERT INTO examenes (nota, id_curso, id_alumno) VALUES (?, ?, ?)", (6, 1, 9))
    c.execute("INSERT INTO examenes (nota, id_curso, id_alumno) VALUES (?, ?, ?)", (3.5, 1, 10))

    c.execute("INSERT INTO examenes (nota, id_curso, id_alumno) VALUES (?, ?, ?)", (7, 2, 1))
    c.execute("INSERT INTO examenes (nota, id_curso, id_alumno) VALUES (?, ?, ?)", (7, 2, 2))
    c.execute("INSERT INTO examenes (nota, id_curso, id_alumno) VALUES (?, ?, ?)", (8.5, 2, 3))
    c.execute("INSERT INTO examenes (nota, id_curso, id_alumno) VALUES (?, ?, ?)", (8, 2, 4))
    c.execute("INSERT INTO examenes (nota, id_curso, id_alumno) VALUES (?, ?, ?)", (9, 2, 5))
    c.execute("INSERT INTO examenes (nota, id_curso, id_alumno) VALUES (?, ?, ?)", (7.5, 2, 6))
    c.execute("INSERT INTO examenes (nota, id_curso, id_alumno) VALUES (?, ?, ?)", (7, 2, 7))
    c.execute("INSERT INTO examenes (nota, id_curso, id_alumno) VALUES (?, ?, ?)", (10, 2, 8))
    c.execute("INSERT INTO examenes (nota, id_curso, id_alumno) VALUES (?, ?, ?)", (9, 2, 9))
    c.execute("INSERT INTO examenes (nota, id_curso, id_alumno) VALUES (?, ?, ?)", (7.5, 2, 10))

    conn.commit()
    conn.close()