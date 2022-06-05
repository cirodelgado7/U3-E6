from zope.interface import implementer

from ClaseNodo import Nodo
from IAparato import IAparato
from ClaseTelevisor import Televisor
from ClaseHeladera import Heladera
from ClaseLavarropa import Lavarropa


@implementer(IAparato)
class Lista:
    __comienzo = None
    __actual = None
    __indice = 0
    __tope = 0

    def __init__(self):
        self.__comienzo = None
        self.__actual = None

    def __iter__(self):
        return self

    def __next__(self):
        if self.__indice == self.__tope:
            self.__actual = self.__comienzo
            self.__indice = 0
            raise StopIteration
        else:
            self.__indice += 1
            dato = self.__actual.getDato()
            self.__actual = self.__actual.getSiguiente()
            return dato

    def toJSON(self):
        return dict(
            __class__=self.__class__.__name__,
            Nodos=[Lista.toJSON() for Lista in self]
        )

    def insertarAparato(self, unAparato, indice):  # insertar adentro
        aux = self.__comienzo
        bandera = False
        c = 0
        if indice <= self.__tope:
            if c == indice:
                if self.__comienzo is None:
                    nuevoNodo = Nodo(unAparato)
                    nuevoNodo.setSiguiente(self.__comienzo)
                    self.__actual = nuevoNodo
                    self.__tope += 1
                else:
                    nuevoNodo = Nodo(unAparato)
                    nuevoNodo.setSiguiente(self.__comienzo)
                    aux.setSiguiente(aux.getSiguiente())
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
                        aux = aux.getSiguiente()
                if c == indice:
                    nuevoNodo = Nodo(unAparato)
                    ant.setSiguiente(nuevoNodo)
                    nuevoNodo.setSiguiente(aux)
                    self.__tope += 1
        else:
            raise Exception('El índice no es válido')

    def agregarAparato(self, artefacto):
        nodo = Nodo(artefacto)
        nodo.setSiguiente(self.__comienzo)
        self.__comienzo = nodo
        self.__actual = nodo
        self.__tope += 1

    def listarDatosAparatos(self):
        aux = self.__comienzo
        while aux != None:
            print(aux.getDato())
            aux = aux.getSiguiente()

    def mostrarAparato(self, indice):
        aux = self.__comienzo
        i = 0
        bandera = True
        while aux != None and bandera:
            if indice == i:
                bandera = False
            else:
                i += 1
                aux = aux.getSiguiente()
        if indice == i:
            if isinstance(aux.getDato(), Televisor):
                print("Tipo de aparato: Televisor")
            elif isinstance(aux.getDato(), Heladera):
                print("Tipo de aparato: Heladera")
            else:
                print("Tipo de aparato: Lavarropa")
        else:
            print('No se encontró ningún artefacto')

    def mostrarPhilips(self):
        aux = self.__comienzo
        contT = 0
        contH = 0
        contL = 0
        # print(aux.getDato().getMarca())
        while aux != None:
            if aux.getDato().getMarca() == 'Philips':
                if isinstance(aux.getDato(), Televisor):
                    contT += 1
                elif isinstance(aux.getDato(), Heladera):
                    contH += 1
                elif isinstance(aux.getDato(), Lavarropa):
                    contL += 1
            aux = aux.getSiguiente()
        print('Cantidad por marca Philips: Teles: {} Heladeras: {} Lavarropas: {}'.format(contT, contH, contL))

    def listarDatosAparatos(self):
        aux = self.__comienzo
        while aux != None:
            print('\nMarca: {}'.format(aux.getDato().getMarca()))
            print('Pais de fabricacion: {}'.format(aux.getDato().getPais()))
            print('Importe: {:.2f}'.format(float(aux.getDato().getImporte())))
            aux = aux.getSiguiente()

    def buscaTipoLavarropa(self):  # inciso 5
        aux = self.__comienzo
        while aux != None:
            if isinstance(aux.getDato(), Lavarropa):
                if aux.getDato().getTipo() == 'Superior':
                    print('Marca de lavarropas con carga Superiror: ')
                    print(aux.getDato().getMarca())
            aux = aux.getSiguiente()

    def mostrarTodaLista(self):
        aux = self.__comienzo
        while aux != None:
            print(aux.getDato())
            aux = aux.getSiguiente()
