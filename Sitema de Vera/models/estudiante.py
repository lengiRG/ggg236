class Estudiante:
    def __init__(self, id, nombre, apellido, email, carnet):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.carnet = carnet

    def a_diccionario(self):
        return self.__dict__

    @classmethod
    def desde_diccionario(cls, datos):
        return cls(datos["id"], datos["nombre"], datos["apellido"],
                   datos["email"], datos["carnet"])

    def __str__(self):
        return f"{self.id} - {self.carnet} - {self.nombre} {self.apellido}"
