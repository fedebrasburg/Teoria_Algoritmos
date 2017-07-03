from creador_grafos import crearGrafoConexo, crearGrafoCompleto
from parser import Parser
from os.path import isfile
from random import randint
from math import log, sqrt, pow, ceil
from copy import deepcopy
from itertools import combinations
import sys

INFINITO = float("inf")

"""Correr como python karger.py n, con n la cantidad de vertices del grafo"""


class Karger(object):
    def __init__(self, g, m):
        # Como llamo 2 veces, necesito que el grafo original g se mantenga intacto para el segundo llamado
        self.grafo = deepcopy(g)
        self.m = m
        # Aca se guardara el set al que pertenezcan
        self.corte = {i: [i] for i in self.grafo.devolver_vertices()}

    def contraer(self, id1, id2):
        for destino, aristas in self.grafo.devolver_aristas()[id2].items():
            # Me fijo que cantidad de aristas hay entre ellos
            cantidad_aristas = len(aristas)
            # Borro las aristas originales del grafo
            self.grafo.borrar_arista_no_dirigida(id2, destino)
            # Si la arista a agregar no es una arista entre id1 e id2, agrego tantas como saque
            if destino != id1:
                for _ in range(cantidad_aristas):
                    self.grafo.agregar_arista_no_dirigida(id1, destino)
        # Borro el vertice que contraje, que se fusiono con id1
        self.grafo.borrar_vertice(id2)
        # Actualizo el set al que pertenece el vertice id2
        self.corte[id1] += self.corte[id2]
        # Borro la key id2 del diccionario
        self.corte.pop(id2, None)

    def karger(self):
        if self.grafo.devolver_cant_vertices() == self.m:
            return self.grafo
        aristas = self.grafo.devolver_aristas_list()
        aristaRandom = aristas[randint(0, len(aristas) - 1)]
        # De esta forma me aseguro que id1 siempre sea menor que id2
        self.contraer(min(aristaRandom.id1, aristaRandom.id2), max(aristaRandom.id1, aristaRandom.id2))
        return self.karger()


def grafoInicial(n):
    path = '../out/grafoKarger.txt'
    # Verifico que el archivo, si ya esta creado, sea de la misma cantidad de nodos
    if isfile(path) and int(open(path).readline()) == n:
        p = Parser()
        return p.leer_grafo_no_dirigido(path)
    else:
        return crearGrafoConexo(n, path)
        # return crearGrafoCompleto(n, path)


def tamanoCorte(particion1, particion2, aristas):
    tamano = 0
    for i in particion1:
        for j in particion2:
            if i in aristas and j in aristas[i]:
                tamano += len(aristas[i][j])
    return tamano


def fuerzaBruta(g):
    vertices = set(g.devolver_vertices())
    aristas = g.devolver_aristas()
    # Genero todos los subsets de vertices
    particiones = [set(j) for i in range(len(vertices)) for j in combinations(vertices, i + 1)]
    particiones.remove(vertices)  # Saco el subset que es exactamente vertices
    tamanoMin = INFINITO
    for particion in particiones:
        corte = tamanoCorte(particion, vertices - particion, aristas)
        if corte < tamanoMin:
            tamanoMin = corte
    return tamanoMin


def mejorEstimacion(g):
    n = g.devolver_cant_vertices()
    if n > 8:
        k1 = Karger(g, int(ceil(n / sqrt(2) + 1)))
        X1 = mejorEstimacion(k1.karger())
        k2 = Karger(g, int(ceil(n / sqrt(2) + 1)))
        X2 = mejorEstimacion(k2.karger())
        return min(X1, X2)
    else:
        return fuerzaBruta(g)


if len(sys.argv) != 2:
    print 'Se debe especificar el parametro n como argumento. Correr python karger.py 10, por ejemplo.'
    exit()
n = int(sys.argv[1])  # Cantidad de vertices
aristas_minimas = 2 * n + 1
for _ in range(int(pow(log(n), 2))):
    g = grafoInicial(n)
    cant_aristas = mejorEstimacion(g)
    if cant_aristas < aristas_minimas:
        aristas_minimas = cant_aristas
print 'Siendo alfa > 2:'
print 'El corte minimo encontrado es', str(aristas_minimas), 'con probabilidad al menos (1 - (1 /',\
    str(n), '^ 1/alfa ) ) =', str(1 - (1 / sqrt(n)))
