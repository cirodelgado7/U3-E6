from Menu import Menu
from ObjectEncoder import ObjectEncoder


if __name__ == "__main__":
    encoder = ObjectEncoder()
    try:
        lista = encoder.decodificarDiccionario(encoder.reader("vehiculos.json"))
        for nodo in lista:
            print(nodo)
        menu = Menu()
        menu.mostrarMenu(lista)
        encoder.writer(lista.toJSON(), "vehiculos.json")
        del encoder
    except FileNotFoundError:
        print('No es posible abrir el archivo')