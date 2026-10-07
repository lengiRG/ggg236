class Asignatura:
    def __init__(self, id, nombre, codigo):
        self.id = id
        self.nombre = nombre
        self.codigo = codigo

    def a_diccionario(self):
        return self.__dict__

    @classmethod
    def desde_diccionario(cls, datos):
        return cls(datos["id"], datos["nombre"], datos["codigo"])

    def __str__(self):
        return f"{self.id} - {self.codigo} - {self.nombre}"
