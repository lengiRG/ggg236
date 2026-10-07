class InterfazConsola:
    @staticmethod
    def titulo(texto):
        print("\n" + "=" * 45)
        print(texto)
        print("=" * 45)

    @staticmethod
    def mostrar_lista(lista):
        if not lista:
            print("No hay registros.")
        else:
            for objeto in lista:
                print(objeto)

    @staticmethod
    def pedir_id():
        try:
            return int(input("Ingrese ID: "))
        except ValueError:
            return None

    @staticmethod
    def mensaje(texto):
        print(texto)
