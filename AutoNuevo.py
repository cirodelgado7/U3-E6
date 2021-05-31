from Auto import Auto


class AutoNuevo(Auto):

    __vesion = str

    marca = "Peugeot"

    def __init__(self, modelo, cantidadPuertas, color, precioBase, version):
        super().__init__(modelo, cantidadPuertas, color, precioBase)
        self.__vesion = version.lower()

    def __str__(self):
        cadena = '\nMarca: {}'.format(self.getMarca())
        cadena += '\nModelo: {}'.format(self.getModelo())
        cadena += '\nVersión: {}'.format(self.__vesion)
        cadena += '\nCantidad de Puertas: {}'.format(self.getCantidadPuertas())
        cadena += '\nColor: {}'.format(self.getColor())
        cadena += '\nPrecio: ${:.2f}'.format(self.getPrecioBase())
        return cadena

    def getversion(self):
        return self.__vesion

    @classmethod
    def getMarca(cls):
        return cls.marca

    def getImporteVenta(self):
        if self.__vesion == "full":
            importe = self.getPrecioBase() + self.getPrecioBase() * 0.12
        else:
            importe = self.getPrecioBase() + self.getPrecioBase() * 0.1
        return importe

    def obtenerVehiculo(self):
        return self.getModelo() + '-' + self.getMarca()

    def mostrarAuto(self):
        cadena = 'Marca: {}'.format(self.getMarca)
        cadena += 'Versión: {}'.format(self.__vesion)
        cadena += super(AutoNuevo, self).mostrarAuto()

    def toJSON(self):
        return dict(
            __class__=self.__class__.__name__,
            __atributos__=dict(
                modelo=self.getModelo(),
                precioBase=self.getPrecioBase(),
                color=self.getColor(),
                cantidadPuertas=self.getCantidadPuertas(),
                version=self.__vesion,
            )
        )
