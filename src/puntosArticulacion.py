from grafo import Grafo
from parser import Parser
from dfs import DFS
import time

"""Utilizar como python puntosArticulacion.py"""

def PuntosArticulacion(g):
    """Dado un grafo no dirigido, devuelve los puntos de articulacion"""
    dfs = DFS(g)
    print dfs.get_bosque_DFS()
    return dfs.get_puntos_artic()

for i in [0, 7, 1]:
    start = time.time()
    parser = Parser()
    g = parser.leerGrafoNoDirigido("../in/ej2/g"+str(i)+".txt")
    print PuntosArticulacion(g)
    end = time.time()
    print("Con " + str(g.devolver_cant_vertices()) + " vertices y " + str(len(g.devolver_aristas())) + " aristas, tardo: " + str(end - start) + " segundos")