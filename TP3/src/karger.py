from creador_grafos import crearGrafoConexo
from parser import Parser
from os.path import isfile
from random import randint
from grafo import Grafo


class Karger(object):
    def __init__(self, n):
        path = "../out/grafoKarger.txt"
        if not isfile(path):
            self.grafo = crearGrafoConexo(n, path)
        else:
            # p = Parser()
            # self.grafo = p.leer_grafo_no_dirigido(path)
            self.grafo = Grafo()
            self.grafo.agregar_vertice(0)
            self.grafo.agregar_vertice(1)
            self.grafo.agregar_vertice(2)
            self.grafo.agregar_vertice(3)
            self.grafo.agregar_arista_no_dirigida(0, 1)
            self.grafo.agregar_arista_no_dirigida(1, 2)
            self.grafo.agregar_arista_no_dirigida(2, 3)
            self.grafo.agregar_arista_no_dirigida(3, 0)
            self.grafo.agregar_arista_no_dirigida(0, 2)
        self.corte = {i:[i] for i in range(self.grafo.devolver_cant_vertices())}  # Aca se guardara el set al que pertenezcan

    def contraer(self, id1, id2):
        # print 'Empezando la contraccion de', id1, 'hacia', id2
        for destino, arista in self.grafo.devolver_aristas()[id2].items():
            # Si la arista a agregar no es una arista entre id1 e id2
            if destino != id1:
                # print '\tAgregando arista', id1, 'a', destino
                self.grafo.agregar_arista_no_dirigida(id1, destino)
            # Borro la arista original del grafo
            # print '\tBorrando arista', id2, 'a', destino
            self.grafo.borrar_arista_no_dirigida(id2, destino)
        # Borro el vertice que contraje, que se fusiono con id1
        # print '\tBorrando vertice', id2
        self.grafo.borrar_vertice(id2)
        # Actualizo el set al que pertenece el vertice id2
        self.corte[id1] += self.corte[id2]
        # Borro la key id2 del diccionario
        self.corte.pop(id2, None)

    def karger(self):
        if self.grafo.devolver_cant_vertices() == 2:
            return self.corte, len(self.grafo.devolver_aristas_list()) / 2
        aristas = self.grafo.devolver_aristas_list()
        aristaRandom = aristas[randint(0, len(aristas) - 1)]
        # print 'La arista a contraer es', aristaRandom
        # De esta forma me aseguro que id1 siempre sea menor que id2
        self.contraer(min(aristaRandom.id1, aristaRandom.id2), max(aristaRandom.id1, aristaRandom.id2))
        return self.karger()

resultDos = []
resultTres = []
n = 10
m = 10000
for _ in range(n):
    dos = 0
    tres = 0
    for _ in range(m):
        k = Karger(5)
        corte, aristas = k.karger()
        if aristas == 2: dos +=1
        if aristas == 3: tres +=1
    resultDos.append(dos)
    resultTres.append(tres)
print "Dos: " + str(sum(resultDos)/float(n)/100)
print "Tres: " + str(sum(resultTres)/float(n)/100)
