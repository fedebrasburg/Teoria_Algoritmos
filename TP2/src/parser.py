from grafo import Grafo

CERO = 0
UNO = 1


class Parser(object):
    def leer_grafo_no_dirigido(self, nombre):
        """Lee un archivo de un grafo no dirigido sin peso"""
        try:
            grafo = Grafo()
            grafo.leer_no_dirigido(nombre)
            return grafo
        except:
            print "Ocurrio un error leyendo el archivo de grafo no dirigido " + nombre
            return False

    def leer_grafo_dirigido(self, nombre):
        """Lee un archivo de un grafo dirigido sin peso"""
        try:
            grafo = Grafo()
            grafo.leer_dirigido(nombre)
            return grafo
        except:
            print "Ocurrio un error leyendo el archivo de grafo dirigido " + nombre
            return False
