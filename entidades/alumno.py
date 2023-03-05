class Alumno:
    def __init__(self, id, alias, email):
        self.id = id
        self.desvio_estandar = 0
        self.alias = alias
        self.email = email

    def setear_desvio(self, desvio):
        self.desvio_estandar = desvio

    def __str__(self) -> str:
        return "Id: " + str(self.id) + ", alias: " + self.alias + ", email: " + self.email