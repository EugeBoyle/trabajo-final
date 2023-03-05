class Curso:
    def __init__(self, id, nombre, duracion):
        self.id = id
        self.nombre = nombre
        self.duracion = duracion

    def __str__(self) -> str:
        return "Id: " + str(self.id) + ", nombre: " + self.nombre + ", duracion: " + self.duracion