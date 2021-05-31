from zope.interface import implementer
from Nodo import Nodo
from IAuto import IAuto
from AutoNuevo import AutoNuevo
from AutoUsado import AutoUsado


@implementer(IAuto)

class Lista(object):

    __comienzo = None
    __actual = None
    __indice = 0
    __tope = 0

    def __init__(self):
        self.__comienzo = None
        self.__actual = None
        self.__indice = 0
        self.__tope = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.__indice is self.__tope:
            self.__actual = self.__comienzo
            self.__indice = 0
            raise StopIteration
        else:
            self.__indice += 1
            dato = self.__actual.getDato()
            self.__actual = self.__actual.getSig()
            return dato

    def __len__(self):
        return self.__tope

    def insertarAuto(self, Auto):
        indice = int(input('Ingrese la posición en la que lo desea ubicar: '))
        aux = self.__comienzo
        bandera = False
        c = 0
        if indice <= self.__tope:
            if c == indice:
                if self.__comienzo is None:
                    nuevoNodo = Nodo(Auto)
                    nuevoNodo.setSig(self.__comienzo)
                    self.__actual = nuevoNodo
                    self.__tope += 1
                else:
                    nuevoNodo = Nodo(Auto)
                    nuevoNodo.setSig(self.__comienzo)
                    aux.setSig(aux.getSig())
                    self.__comienzo = nuevoNodo
                    self.__actual = nuevoNodo
                    self.__tope += 1
            else:
                ant = aux
                while aux is not None and bandera is False:
                    if c == indice:
                        bandera = True
                    else:
                        c += 1
                        ant = aux
                        aux = aux.getSig()
                if c == indice:
                    nuevoNodo = Nodo(Auto)
                    ant.setSig(nuevoNodo)
                    nuevoNodo.setSig(aux)
                    self.__tope += 1
        else:
            raise Exception('El índice no es válido')


    def agregarAuto(self, Auto):
        nuevoNodo = Nodo(Auto)
        aux = self.__comienzo
        if aux is None:
            self.__comienzo = nuevoNodo
            self.__actual = nuevoNodo
            self.__tope += 1
        else:
            ant = aux
            aux = aux.getSig()
            while aux is not None:
                ant = aux
                aux = aux.getSig()
            if aux is None:
                ant.setSig(nuevoNodo)
                self.__tope += 1
                del aux

    def mostrarTipoAuto(self):
        try:
            indice = int(input("Indice de la lista: "))
            aux = self.__comienzo
            i = 0
            while i < indice and aux is not None:
                aux = aux.getSig()
                i += 1
            if aux is None:
                raise IndexError
            else:
                if isinstance(aux.getDato(), AutoNuevo):
                    print("Tipo de Auto: Auto Nuevo")
                else:
                    print("Tipo de Auto: Auto Usado")
        except IndexError:
            print("Posicion Invalida")

    def modificarImporte(self):
        patente = input("Ingrese la patente: ")
        aux = self.__comienzo
        while aux is None and isinstance(aux, AutoUsado) is False and aux.getDato().getPatente() != patente:
            aux = aux.getSig()
        if aux is None:
            return IndexError
        else:
            aux.getDato().setPrecioBase(float(input("Precio Nuevo: ")))
            print("El Nuevo precio de venta es ${:.2f}".format(aux.getDato().getPrecioBase()))

    def mostrarEconomico(self):
        aux = self.__comienzo
        auto = None
        minimo = 999999999
        while aux is not None:
            if minimo > aux.getDato().getPrecioBase():
                minimo = aux.getDato().getPrecioBase()
                auto = aux
                aux = aux.getSig()
            else:
                aux = aux.getSig()
        print(auto.getDato())

    def toJSON(self):
        return dict(
            __class__=self.__class__.__name__,
            Nodos=[Lista.toJSON() for Lista in self]
        )

    def registrarAuto(self):
        op = int(input('1. Nuevo - 2. Usado: '))
        if op == 1:
            print('Marca:', AutoNuevo.marca)
            modelo = input('Modelo: ')
            version = input('Base - Full: ')
            cantidadPuertas = int(input('Cantidad de puertas: '))
            color = input('Color: ')
            precioBase = float(input('Precio Base: '))
            unAuto = AutoNuevo(modelo, cantidadPuertas, color, precioBase, version)
            return unAuto
        elif op == 2:
            marca = input('Marca: ')
            modelo = input('Modelo: ')
            cantidadPuertas = int(input('Cantidad de puertas: '))
            color = input('Color: ')
            precioBase = float(input('Precio Base: '))
            km = float(input('Km: '))
            año = input('Año: ')
            patente = input('Patente: ')
            unAuto = AutoUsado(modelo, cantidadPuertas, color, precioBase, marca, km, año, patente)
            return unAuto
        else:
            print('La opción ingresada no es válida')
