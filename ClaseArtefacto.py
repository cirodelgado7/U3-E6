class Artefacto:
    __marca = ''
    __modelo = ''
    __color = ''
    __paisFabricacion = ''
    __precioBase: float

    def __init__(self, marca, modelo, color, paisFabricacion, precioBase):
        self.__marca = marca
        self.__modelo = modelo
        self.__color = color
        self.__paisFabricacion = paisFabricacion
        self.__precioBase = precioBase

    def __str__(self):
        cadena = 'Marca: {}'.format(self.__marca)
        cadena += 'Modelo: {}'.format(self.__modelo)
        cadena += 'Color: {}'.format(self.__color)
        cadena += 'Pais de Fabricación: {}'.format(self.__paisFabricacion)
        cadena += 'Precio Base: ${:.2f}'.format(self.__precioBase)
        return cadena

    def getPrecioBase(self):
        return self.__precioBase

    def setPrecioBase(self, precioBase):
        self.__precioBase = precioBase

    def getMarca(self):
        return self.__marca

    def getModelo(self):
        return self.__modelo

    def getColor(self):
        return self.__color

    def getPaisFabricacion(self):
        return self.__paisFabricacion
