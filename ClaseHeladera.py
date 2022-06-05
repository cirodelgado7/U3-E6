from ClaseArtefacto import Artefacto


class Heladera(Artefacto):
    __capacidad = ''
    __frezzer = ''
    __ciclica = ''

    def __init__(self, marca, modelo, color, paisFabricacion, precioBase, capacidad, frezzer, ciclica):
        super().__init__(marca, modelo, color, paisFabricacion, precioBase)
        self.__capacidad = capacidad
        self.__frezzer = frezzer
        self.__ciclica = ciclica

    def __str__(self):
        cadena = '\nMarca: ' + self.getMarca()
        cadena += '\nModelo: ' + self.getModelo()
        cadena += '\nColor: ' + self.getColor()
        cadena += '\nPais de Fabricación: ' + self.getPaisFabricacion()
        cadena += '\nPrecio Base: ' + str(self.getPrecioBase())
        cadena += '\nCapacidad: ' + self.__capacidad
        cadena += '\nFrezzer: ' + self.__frezzer
        cadena += '\nCíclica: ' + self.__ciclica
        return cadena

    def toJSON(self):
        return dict(
            __class__=self.__class__.__name__,
            __atributos__=dict(
                marca=self.getMarca(),
                modelo=self.getModelo(),
                precioBase=self.getPrecioBase(),
                color=self.getColor(),
                paisFabricacion=self.getPaisFabricacion(),
                capacidad=self.__capacidad,
                frezzer=self.__frezzer,
                ciclica=self.__ciclica,
            )
        )

    def getPais(self):
        return self.getPaisFabricacion()

    def getImporte(self):
        importe = 0
        if self.__frezzer == 'False':
            importe = self.getPrecioBase() + (float(self.getPrecioBase()) * float(0.01))
        elif self.__frezzer == 'True':
            importe = self.getPrecioBase() + (float(self.getPrecioBase()) * float(0.03))
        if self.__ciclica == 'True':
            importe += self.getPrecioBase() * float(0.10)
        return importe