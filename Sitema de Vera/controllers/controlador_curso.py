from models.curso import Curso
from shared.archivo_json import ArchivoJSON

class ControladorCurso:
    def __init__(self):
        self.archivo = ArchivoJSON("data/cursos.json")

    def _siguiente_id(self):
        datos = self.archivo.leer()
        return max([x["id"] for x in datos], default=0) + 1

    def crear(self, nombre, paralelo):
        nuevo = Curso(self._siguiente_id(), nombre, paralelo)
        datos = self.archivo.leer()
        datos.append(nuevo.a_diccionario())
        return self.archivo.guardar(datos)

    def listar(self):
        return [Curso.desde_diccionario(x) for x in self.archivo.leer()]

    def buscar(self, id):
        for objeto in self.listar():
            if objeto.id == id:
                return objeto
        return None

    def actualizar(self, id, cambios):
        datos = self.archivo.leer()
        for i in range(len(datos)):
            if datos[i]["id"] == id:
                for campo, valor in cambios.items():
                    if campo in datos[i] and campo != "id" and str(valor).strip() != "":
                        datos[i][campo] = valor
                return self.archivo.guardar(datos)
        return False

    def eliminar(self, id):
        datos = self.archivo.leer()
        nuevos = [x for x in datos if x["id"] != id]
        if len(nuevos) == len(datos):
            return False
        return self.archivo.guardar(nuevos)
