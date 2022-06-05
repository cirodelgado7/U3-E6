from zope.interface import Interface


class IAparato(Interface):

    def agregarAparato(Aparato):
        pass

    def insertarAparato(Aparato, pos):
        pass

    def MostrarAparato(indice):
        pass