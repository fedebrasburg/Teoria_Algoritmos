from creador_grafos import crearGrafoConexo
from creador_grafos import crearGrafoCompleto
from parser import Parser
from os.path import isfile
from random import randint
from math import log
import sys

"""Correr como python karger.py n, con n la cantidad de vertices del grafo"""

class Karger(object):
    def __init__(self, n):
        path = "../out/grafoKarger.txt"
        # Verifico que el archivo, si ya esta creado, sea de la misma cantidad de nodos
        if isfile(path) and int(open(path).readline()) == n:
            p = Parser()
            self.grafo = p.leer_grafo_no_dirigido(path)
        else:
            # self.grafo = crearGrafoConexo(n, path)
            self.grafo = crearGrafoCompleto(n, path)
        # Aca se guardara el set al que pertenezcan
        self.corte = {i: [i] for i in range(self.grafo.devolver_cant_vertices())}

    def contraer(self, id1, id2):
        print 'Empezando a contraer', id1, 'con', id2
        print "Las aristas hasta el momento son:", len(self.grafo.devolver_aristas_list())
        print "La cantidad de aristas entre ellos son", len(self.grafo.devolver_aristas()[id1][id2])
        for destino, arista in self.grafo.devolver_aristas()[id2].items():
            # Me fijo que cantidad de aristas hay entre ellos
            cantidad_aristas = len(self.grafo.devolver_aristas()[id2][destino])
            # Borro las aristas originales del grafo
            print "Borrando arista de", id2, "a", destino
            self.grafo.borrar_arista_no_dirigida(id2, destino)
            # Si la arista a agregar no es una arista entre id1 e id2, agrego tantas como saque
            if destino != id1:
                for _ in range(cantidad_aristas):
                    print "Agregando arista de", id1, "a", destino
                    self.grafo.agregar_arista_no_dirigida(id1, destino)
        # Borro el vertice que contraje, que se fusiono con id1
        print "Borrando vertice", id2
        self.grafo.borrar_vertice(id2)
        # Actualizo el set al que pertenece el vertice id2
        self.corte[id1] += self.corte[id2]
        # Borro la key id2 del diccionario
        self.corte.pop(id2, None)

    def karger(self):
        print 'Llamando a Karger'
        if self.grafo.devolver_cant_vertices() == 2:
            print self.grafo.devolver_aristas()
            return self.corte, len(self.grafo.devolver_aristas_list()) / 2
        aristas = self.grafo.devolver_aristas_list()
        aristaRandom = aristas[randint(0, len(aristas) - 1)]
        print 'La arista a contraer es', aristaRandom
        # De esta forma me aseguro que id1 siempre sea menor que id2
        self.contraer(min(aristaRandom.id1, aristaRandom.id2), max(aristaRandom.id1, aristaRandom.id2))
        return self.karger()


if len(sys.argv) != 2:
    print "Se debe especificar el parametro n como argumento. Correr python karger.py 50, por ejemplo."
    exit()
n = int(sys.argv[1])  # Cantidad de vertices
combinatorio = float(n * (n - 1)) / 2
corte_minimo = []
aristas_minimas = 2 * n
# for i in range(int(combinatorio * log(n))):
    # print 'Iteracion', i
k = Karger(n)
corte, cant_aristas = k.karger()
if cant_aristas < aristas_minimas:
    aristas_minimas = cant_aristas
    corte_minimo = corte
print "El corte minimo encontrado es con", str(aristas_minimas), "con probabilidad al menos", str(1 - (1 / float(n))), "siendo el corte", corte_minimo
