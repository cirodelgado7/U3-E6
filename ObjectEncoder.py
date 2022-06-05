import json
from pathlib import Path
from ClaseTelevisor import Televisor
from ClaseHeladera import Heladera
from ClaseLavarropa import Lavarropa
from Lista import Lista


class ObjectEncoder(object):

    def writer(self, lista, archivo):
        with Path(archivo).open("w", encoding="UTF-8") as destino:
            json.dump(lista, destino, indent=4)
        return True

    def reader(self, archivo):
        with Path(archivo).open("r", encoding="UTF-8") as fuente:
            aux = json.load(fuente)
        return aux

    def decodificarDiccionario(self, d):
        if "__class__" not in d:
            return d
        else:
            class_name = d['__class__']
            class_ = eval(class_name)
            if class_name == 'Lista':
                nodos = d['Nodos']
#               dNodo = nodos[0]
                Lista = class_()
                for i in range(len(nodos)):
                    dNodo = nodos[i]
                    class_name = dNodo.pop('__class__')
                    class_ = eval(class_name)
                    atributos = dNodo['__atributos__']
                    unAparato = class_(**atributos)
                    Lista.agregarAparato(unAparato)
                return Lista