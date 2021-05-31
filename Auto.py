import abc
from abc import ABC


class Auto(ABC):

    __modelo = None
    __cantidadPuertas = int
    __color = None
    __precioBase = float

    def __init__(self, modelo, cantidadPuertas, color, precioBase):
        self.__modelo = modelo
        self.__cantidadPuertas = cantidadPuertas
        self.__color = color
        self.__precioBase = precioBase

    def __str__(self):
        cadena = 'Modelo: {}'.format(self.__modelo)
        cadena += 'Cantidad de Puertas: {}'.format(self.__cantidadPuertas)
        cadena += 'Color: {}'.format(self.__color)
        cadena += 'Precio Base: ${}'.format(self.__precioBase)
        return cadena

    def getPrecioBase(self):
        return self.__precioBase

    def setPrecioBase(self, precioBase):
        self.__precioBase = precioBase

    def getModelo(self):
        return self.__modelo

    def getColor(self):
        return self.__color

    def getCantidadPuertas(self):
        return self.__cantidadPuertas

    def mostrarAuto(self):
        cadena = 'Modelo: {}'.format(self.__modelo)
        cadena += 'Cantidad de Puertas: {}'.format(self.__cantidadPuertas)
        cadena += 'Color: {}'.format(self.__color)
        cadena += 'Precio Base: ${:.2f}'.format(self.__precioBase)
        return cadena

    @abc.abstractmethod
    def getImporteVenta(self):
        pass

    @abc.abstractmethod
    def obtenerVehiculo(self):
        pass

    def toJSON(self):
        return dict(
            __class__=self.__class__.__name__,
            __atributos__=dict(
                modelo=self.getModelo(),
                cantidadPuertas=self.getCantidadPuertas(),
                color=self.getColor(),
                precioBase=self.getPrecioBase()
                )
            )