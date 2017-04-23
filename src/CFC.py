from parser import Parser
from grafo import trasponer
from dfs import DFS
import time

"""Utilizar como python CFC.py"""


class CFC(object):

    def __init__(self, g):
        self.g = g

    def get_CFC(self):
        """Recibe un grafo y devuelve las componentes fuertemente conexas"""
        r = DFS(self.g).hacer_DFS()
        return DFS(trasponer(self.g), sorted(r.get_tiempo_finalizado(), key=r.get_tiempo_finalizado().get, reverse=True)).hacer_DFS().get_bosque_DFS()


for i in [0, 1, 2, 3, 4, 5, 6]:
    start = time.time()
    parser = Parser()
    grafo = parser.leer_grafo_dirigido("../in/ej3/d" + str(i) + ".txt")
    CFC(grafo).get_CFC()
    end = time.time()
    print("Con " + str(grafo.devolver_cant_vertices()) + " vertices y " + str(len(grafo.devolver_aristas())) + " aristas, tardo: " + str(end - start) + " segundos")
