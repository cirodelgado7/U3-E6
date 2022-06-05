from ClaseMenu import Menu
from ObjectEncoder import ObjectEncoder


if __name__ == '__main__':
    encoder = ObjectEncoder()
    lista = None
    try:
        lista = encoder.decodificarDiccionario(encoder.reader("aparatoselectronicos.json"))
        for nodo in lista:
            print(nodo)
        menu = Menu()
        menu.mostrarMenu(lista)
        encoder.writer(lista.toJSON(), "aparatoselectronicos.json")
        del encoder
    except FileNotFoundError:
        print('No es posible abrir el archivo')
        if lista is None:
            print('Lista vacia')
        menu = Menu()
        menu.mostrarMenu(lista)
        encoder.writer(lista.toJSON(), "aparatoselectronicos.json")
        del encoder
