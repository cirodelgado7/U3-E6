from zope.interface import Interface


class IAuto(Interface):

    def agregarAuto(Auto):
        pass

    def insertarAuto(Auto, pos):
        pass

    def MostrarAuto(indice):
        pass