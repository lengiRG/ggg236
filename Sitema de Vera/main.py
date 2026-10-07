from controllers.controlador_estudiante import ControladorEstudiante
from controllers.controlador_docente import ControladorDocente
from controllers.controlador_asignatura import ControladorAsignatura
from controllers.controlador_curso import ControladorCurso
from views.interfaz_consola import InterfazConsola


class SistemaAcademico:
    def __init__(self):
        self.estudiantes = ControladorEstudiante()
        self.docentes = ControladorDocente()
        self.asignaturas = ControladorAsignatura()
        self.cursos = ControladorCurso()
        self.vista = InterfazConsola()

    def menu_crud(self, nombre, controlador):
        while True:
            self.vista.titulo("GESTION DE " + nombre.upper())
            print("1. Crear")
            print("2. Listar")
            print("3. Buscar")
            print("4. Actualizar")
            print("5. Eliminar")
            print("0. Regresar")
            opcion = input("Opcion: ")

            if opcion == "0":
                break

            if opcion == "1":
                if nombre == "estudiantes":
                    ok = controlador.crear(input("Nombre: "), input("Apellido: "),
                                           input("Email: "), input("Carnet: "))
                elif nombre == "docentes":
                    ok = controlador.crear(input("Nombre: "), input("Apellido: "),
                                           input("Email: "))
                elif nombre == "asignaturas":
                    ok = controlador.crear(input("Nombre: "), input("Codigo: "))
                else:
                    ok = controlador.crear(input("Nombre: "), input("Paralelo: "))
                self.vista.mensaje("Guardado correctamente" if ok else "No se pudo guardar")

            elif opcion == "2":
                self.vista.mostrar_lista(controlador.listar())

            elif opcion == "3":
                id = self.vista.pedir_id()
                objeto = controlador.buscar(id) if id is not None else None
                self.vista.mensaje(str(objeto) if objeto else "Registro no encontrado")

            elif opcion == "4":
                id = self.vista.pedir_id()
                if id is None:
                    self.vista.mensaje("ID incorrecto")
                    continue

                cambios = {}
                if nombre in ("estudiantes", "docentes"):
                    cambios["nombre"] = input("Nuevo nombre (ENTER mantiene): ")
                    cambios["apellido"] = input("Nuevo apellido (ENTER mantiene): ")
                    cambios["email"] = input("Nuevo email (ENTER mantiene): ")
                    if nombre == "estudiantes":
                        cambios["carnet"] = input("Nuevo carnet (ENTER mantiene): ")
                elif nombre == "asignaturas":
                    cambios["nombre"] = input("Nuevo nombre (ENTER mantiene): ")
                    cambios["codigo"] = input("Nuevo codigo (ENTER mantiene): ")
                else:
                    cambios["nombre"] = input("Nuevo nombre (ENTER mantiene): ")
                    cambios["paralelo"] = input("Nuevo paralelo (ENTER mantiene): ")

                ok = controlador.actualizar(id, cambios)
                self.vista.mensaje("Actualizado" if ok else "No se encontro el registro")

            elif opcion == "5":
                id = self.vista.pedir_id()
                ok = controlador.eliminar(id) if id is not None else False
                self.vista.mensaje("Eliminado" if ok else "No se encontro el registro")

            else:
                self.vista.mensaje("Opcion incorrecta")

    def ejecutar(self):
        while True:
            self.vista.titulo("SISTEMA ACADEMICO")
            print("1. Estudiantes")
            print("2. Docentes")
            print("3. Asignaturas")
            print("4. Cursos")
            print("0. Salir")
            opcion = input("Opcion: ")

            if opcion == "1":
                self.menu_crud("estudiantes", self.estudiantes)
            elif opcion == "2":
                self.menu_crud("docentes", self.docentes)
            elif opcion == "3":
                self.menu_crud("asignaturas", self.asignaturas)
            elif opcion == "4":
                self.menu_crud("cursos", self.cursos)
            elif opcion == "0":
                print("Programa finalizado")
                break
            else:
                print("Opcion incorrecta")


if __name__ == "__main__":
    sistema = SistemaAcademico()
    sistema.ejecutar()
