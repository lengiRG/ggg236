class Docente:
    def __init__(self, id, nombre, apellido, email):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.email = email

    def a_diccionario(self):
        return self.__dict__

    @classmethod
    def desde_diccionario(cls, datos):
        return cls(datos["id"], datos["nombre"], datos["apellido"], datos["email"])

    def __str__(self):
        return f"{self.id} - {self.nombre} {self.apellido} - {self.email}"
