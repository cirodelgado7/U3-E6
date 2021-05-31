from AutoNuevo import AutoNuevo


class Menu:

    __switcher = None

    def __init__(self):
        self.__switcher = {
                            1: self.opcion1,
                            2: self.opcion2,
                            3: self.opcion3,
                            4: self.opcion4,
                            5: self.opcion5,
                            6: self.opcion6,
                            7: self.salir
                            }

    def mostrarMenu(self, lista):
        salir = False
        while not salir:
            print("\n*********** Consecionaria TuAuto.com *******************")
            print("********************* Menu *****************************\n"
                  "1. Insertar un Auto en cualquier posición de la colección"
                  "\n2. Agregar un Auto al final de la colección"
                  "\n3. Mostrar un tipo de Auto de la colección"
                  "\n4. Modifificar precio de un Auto Usado"
                  "\n5. Mostrar el auto más económico"
                  "\n6. Mostrar datos de todos los Autos"
                  "\n7. Salir")
            op = int(input('Ingrese una opcion: '))
            if op in range(1, 8) and type(op) is not str:
                self.opcion(op, lista)
                salir = op == 7
            else:
                print('La opción ingresada no es valida. Ingrese una opción válida')

    def getSwitcher(self):
        return self.__switcher

    def opcion(self, op, lista):
        func = self.__switcher.get(op, lambda: print("Opción no válida"))
        func(lista)

    def opcion1(self, lista):
        print('\n1. Insertar un Auto en cualquier posición de la colección')
        auto = lista.registrarAuto()
        lista.insertarAuto(auto)

    def opcion2(self, lista):
        print('\n2. Agregar un Auto al final de la colección')
        auto = lista.registrarAuto()
        lista.agregarAuto(auto)

    def opcion3(self, lista):
        print('\n3. Mostrar un tipo de Auto de la colección')
        lista.mostrarTipoAuto()

    def opcion4(self, lista):
        print('\n4. Modifificar precio de un Auto Usado')
        lista.modificarImporte()

    def opcion5(self, lista):
        print('\n5. Mostrar el auto más económico')
        lista.mostrarEconomico()

    def opcion6(self, lista):
        print('\n6. Mostrar datos de todos los Autos')
        lista.mostrarTodos()

    def salir(self, lista):
        print('\n Los datos fueron guardados en el archivo vehiculos.json')
