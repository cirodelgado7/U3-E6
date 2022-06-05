from ClaseArtefacto import Artefacto


class Televisor(Artefacto):
    __tipoPantalla = ''
    __pulgadas = ''
    __tipoDefinicion = ''
    __conexionInternet = ''

    def __init__(self, marca, modelo, color, paisFabricacion, precioBase, tipoPantalla, pulgadas, tipoDefinicion,
                 conexionInternet):
        super().__init__(marca, modelo, color, paisFabricacion, precioBase)
        self.__tipoPantalla = tipoPantalla
        self.__pulgadas = pulgadas
        self.__tipoDefinicion = tipoDefinicion
        self.__conexionInternet = conexionInternet

    def __str__(self):
        cadena = '\nMarca: ' + self.getMarca()
        cadena += '\nModelo: ' + self.getModelo()
        cadena += '\nColor: ' + self.getColor()
        cadena += '\nPais de Fabricación: ' + self.getPaisFabricacion()
        cadena += '\nPrecio Base: ' + str(self.getPrecioBase())
        cadena += '\nTipo de Pantalla: ' + self.__tipoPantalla
        cadena += '\nPulgadas: ' + self.__pulgadas
        cadena += '\nTipo de Definición: ' + self.__tipoDefinicion
        cadena += '\nConexión a Internet: ' + self.__conexionInternet
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
                tipoPantalla=self.__tipoPantalla,
                pulgadas=self.__pulgadas,
                tipoDefinicion=self.__tipoDefinicion,
                conexionInternet=self.__conexionInternet
            )
        )

    def getPais(self):
        return self.getPaisFabricacion()

    def getImporte(self):
        importe = 0
        if self.__tipoDefinicion == 'SD':
            importe = self.getPrecioBase() + (self.getPrecioBase() * float(0.01))
        elif self.__tipoDefinicion == 'HD':
            importe = self.getPrecioBase() + (self.getPrecioBase() * float(0.02))
        elif self.__tipoDefinicion == 'FULL HD':
            importe = self.getPrecioBase() + (self.getPrecioBase() * float(0.03))
        if self.__conexionInternet == 'True':
            importe += self.getPrecioBase() * 0.10
        return importe