class Curso:
    def __init__(self, id, nombre, paralelo):
        self.id = id
        self.nombre = nombre
        self.paralelo = paralelo

    def a_diccionario(self):
        return self.__dict__

    @classmethod
    def desde_diccionario(cls, datos):
        return cls(datos["id"], datos["nombre"], datos["paralelo"])

    def __str__(self):
        return f"{self.id} - {self.nombre} - Paralelo {self.paralelo}"
