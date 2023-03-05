class Alumno:
    def __init__(self, id, alias, email):
        self.desvio_estandar = 0
        self.alias = alias
        self.email = email

    def setear_desvio(self, desvio):
        self.desvio_estandar = desvio
