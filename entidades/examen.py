class Examen:
    def __init__(self, id, nota, id_curso, id_alumno):
        self.id = id
        self.nota = nota
        self.id_curso = id_curso
        self.id_alumno = id_alumno
    
    def Obtener_nota(self):
       return self.nota