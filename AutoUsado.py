from Auto import Auto
from datetime import date


class AutoUsado(Auto):

    __marca = ''
    __km = 0
    __año = 0
    __patente = ''

    def __init__(self, modelo, cantidadPuertas, color, precioBase, marca, km, año, patente):
        super().__init__(modelo, cantidadPuertas, color, precioBase)
        self.__marca = marca
        self.__km = km
        self.__año = año
        self.__patente = patente

    def __str__(self):
        cadena = '\nMarca: {}'.format(self.__marca)
        cadena += '\nModelo: {}'.format(self.getModelo())
        cadena += '\nCantidad de Puertas: {}'.format(self.getCantidadPuertas())
        cadena += '\nColor: {}'.format(self.getColor())
        cadena += '\nKm: {}'.format(self.__km)
        cadena += '\nAño: {}'.format(self.__año)
        cadena += '\nPatente: {}'.format(self.__patente)
        cadena += '\nPrecio: ${:.2f}'.format(self.getPrecioBase())
        return cadena

    def getMarca(self):
        return self.__marca

    def getKm(self):
        return self.__km

    def getAño(self):
        return self.__año

    def getPatente(self):
        return self.__patente

        def getImporteVenta(self):
        if self.__km < 100000:
            importe = self.getPrecioBase() - (int(date.today().year) - int(self.__año)) * 0.01 * self.getPrecioBase()
        else:
            importe = self.getPrecioBase() - (int(date.today().year) - int(self.__año)) * 0.02 * self.getPrecioBase()
        return importe

    def obtenerVehiculo(self):
        return self.getModelo() + '-' + self.getMarca()

    def toJSON(self):
        return dict(
            __class__=self.__class__.__name__,
            __atributos__=dict(
                modelo=self.getModelo(),
                cantidadPuertas=self.getCantidadPuertas(),
                color=self.getColor(),
                precioBase=self.getPrecioBase(),
                marca=self.getMarca(),
                km=self.getKm(),
                año=self.getAño(),
                patente=self.getPatente()
            )
        )

    def mostrarAuto(self):
        cadena = "\nMarca: {}".format(self.__marca)
        cadena += super(AutoUsado, self).__str__()
        cadena += "\nKm: {}".format(self.__km)
        cadena += "\nAño: {}".format(self.__año)
        cadena += "\nPatente: {}".format(self.__patente)
        return cadena
