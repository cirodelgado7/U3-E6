from ClaseTelevisor import Televisor
from ClaseHeladera import Heladera
from ClaseLavarropa import Lavarropa


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
            print("\n************** Empresa Comercial *********************")
            print("********************* Menu *****************************\n"
                  "1. Insertar un aparato en cualquier posición de la colección"
                  "\n2. Agregar un aparato a la colección"
                  "\n3. Mostrar un tipo de aparato de la colección"
                  "\n4. Cantidad de aparatos Philips"
                  "\n5. Mostrar la marca de todos los lavarropas que tienen carga superior"
                  "\n6. Mostrar para todos los aparatos que la empresa tiene a la venta, marca, país de fabricación e importe de venta"
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
        print('\n1. Insertar un aparato en cualquier posición de la colección')
        op = int(input('1 - Televisor / 2 - Heladera / 3 - Lavarropas'))
        if op == 1:
            unArtefacto = self.instanciarTelevisor()
            lista.insertarAparato(unArtefacto, int(input('Ingrese la posición en la que lo desea ubicar: ')))
            lista.listarDatosAparatos()
        elif op == 2:
            unArtefacto = self.instanciarHeladera()
            lista.insertarAparato(unArtefacto, int(input('Ingrese la posición en la que lo desea ubicar: ')))
            lista.listarDatosAparatos()
        elif op == 3:
            unArtefacto = self.instanciarLavarropa()
            lista.insertarAparato(unArtefacto, int(input('Ingrese la posición en la que lo desea ubicar: ')))
            lista.listarDatosAparatos()
        else:
            print('La opción ingresada no es valida')

    def opcion2(self, lista):
        print('\n2. Agregar un aparato a la colección')
        op = int(input('1 - Televisor / 2 - Heladera / 3 - Lavarropas'))
        if op == 1:
            unArtefacto = self.instanciarTelevisor()
            lista.agregarAparato(unArtefacto)
            lista.listarDatosAparatos()
        elif op == 2:
            unArtefacto = self.instanciarHeladera()
            lista.agregarAparato(unArtefacto)
            lista.listarDatosAparatos()
        elif op == 3:
            unArtefacto = self.instanciarLavarropa()
            lista.agregarAparato(unArtefacto)
            lista.listarDatosAparatos()
        else:
            print('La opción ingresada no es valida')

    def opcion3(self, lista):
        print('\n3. Mostrar un tipo de aparato de la colección')
        lista.mostrarAparato(int(input("Indice de la lista: ")))

    def opcion4(self, lista):
        print('\n4. Cantidad de aparatos Philips')
        lista.mostrarPhilips()

    def opcion5(self, lista):
        print('\n5. Mostrar la marca de todos los lavarropas que tienen carga superior')
        lista.buscaTipoLavarropa()

    def opcion6(self, lista):
        print('\n6. Mostrar para todos los aparatos que la empresa tiene a la venta, marca, país de fabricación e importe de venta')
        lista.listarDatosAparatos()

    def salir(self, lista):
        print('\n Los datos fueron guardados en el archivo aparatoselectricos.json')

    def instanciarTelevisor(self):
        marca = input('\nMarca: ')
        modelo = input('\nModelo: ')
        color = input('\nColor: ')
        paisFabricacion = input('\nPais de Fabricación: ')
        precioBase = input('\nPrecio base: ')
        pantalla = input('Ingrese tipo de pantalla: crt, vga, svga, plasma, lcd, TouchScreen, MultiTouch: ')
        pulgada = input('Ingrese pulgadas: ')
        definicion = input('Ingrese tipo de definicion: SD, HD, FULL, HD: ')
        internet = input('Conexion a internet, True o False: ')
        unAparato = Televisor(marca, modelo, color, paisFabricacion, precioBase, pantalla, pulgada, definicion,
                              internet)
        return unAparato

    def instanciarHeladera(self):
        marca = input('\nMarca: ')
        modelo = input('\nModelo: ')
        color = input('\nColor: ')
        paisFabricacion = input('\nPais de Fabricación: ')
        precioBase = input('\nPrecio base: ')
        capacidad = input('Capacidad: ')
        frezzer = input('Frezzer: ')
        ciclica = input('Ciclica: ')
        unAparato = Heladera(marca, modelo, color, paisFabricacion, precioBase, capacidad, frezzer, ciclica)
        return unAparato

    def instanciarLavarropa(self):
        marca = input('\nMarca: ')
        modelo = input('\nModelo: ')
        color = input('\nColor: ')
        paisFabricacion = input('\nPais de Fabricación: ')
        precioBase = input('\nPrecio base: ')
        capacidadLavado = input('\nCapacidad de Lavado: ')
        velocidadCentrifugado = input('\nVelocidad de Centrifugado: ')
        cantidadProgramas = input('\nCantidad de Programas: ')
        tipoCarga = input('\nTipo de Carga: ')
        unAparato = Lavarropa(marca, modelo, color, paisFabricacion, precioBase, capacidadLavado, velocidadCentrifugado,
                              cantidadProgramas, tipoCarga)
        return unAparato
