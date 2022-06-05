from ClaseArtefacto import Artefacto


class Lavarropa(Artefacto):
    __capacidadLavado: int
    __velocidadCentrifugado = ''
    __cantidadProgramas = ''
    __tipoCarga = ''

    def __init__(self, marca, modelo, color, paisFabricacion, precioBase, capacidadLavado, velocidadCentrifugado,
                 cantidadProgramas, tipoCarga):
        super().__init__(marca, modelo, color, paisFabricacion, precioBase)
        self.__capacidadLavado = capacidadLavado
        self.__velocidadCentrifugado = velocidadCentrifugado
        self.__cantidadProgramas = cantidadProgramas
        self.__tipoCarga = tipoCarga

    def __str__(self):
        cadena = '\nMarca: ' + self.getMarca()
        cadena += '\nModelo: ' + self.getModelo()
        cadena += '\nColor: ' + self.getColor()
        cadena += '\nPais de Fabricación: ' + self.getPaisFabricacion()
        cadena += '\nPrecio Base: ' + str(self.getPrecioBase())
        cadena += '\nCapacidad de Lavado: ' + str(self.__capacidadLavado)
        cadena += '\nVelocidad de Centrifugado: ' + self.__velocidadCentrifugado
        cadena += '\nCantidad de Programas: ' + self.__cantidadProgramas
        cadena += '\nTipo de Carga: ' + self.__tipoCarga
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
                capacidadLavado=self.__capacidadLavado,
                velocidadCentrifugado=self.__velocidadCentrifugado,
                cantidadProgramas=self.__cantidadProgramas,
                tipoCarga=self.__tipoCarga
            )
        )

    def getTipo(self):
        return self.__tipoCarga

    def getPais(self):
        return self.getPaisFabricacion()

    def getImporte(self):
        importe = 0
        if self.__capacidadLavado <= 5:
            importe = self.getPrecioBase() + (self.getPrecioBase() * float(0.01))
        elif self.__capacidadLavado > 5:
            importe = self.getPrecioBase() + (self.getPrecioBase() * float(0.03))
        return importe