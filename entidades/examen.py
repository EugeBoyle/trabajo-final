class Examen:
    def __init__(self, nota, id_curso, id_alumno):
        self.nota = nota
        self.id_curso = id_curso
        self.id_alumno = id_alumno
    
    def Obtener_nota(self):
       return self.nota