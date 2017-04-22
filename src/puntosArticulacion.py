from parser import Parser
from dfs import DFS
from dfs_iterativo import DFS_iterativo2
import time

"""Utilizar como python puntosArticulacion.py"""

def PuntosArticulacion(g):
    """Dado un grafo no dirigido, devuelve los puntos de articulacion"""
    dfs = DFS_iterativo2(g)
    return dfs.get_puntos_artic()

for i in [0, 7, 1, 2, 3, 4, 5, 6]:
    start = time.time()
    parser = Parser()
    g = parser.leerGrafoNoDirigido("../in/ej2/g"+str(i)+".txt")
    puntos_artic = PuntosArticulacion(g)
    print "Hay", len(puntos_artic), "puntos de articulacion:"#, puntos_artic
    end = time.time()
    print("Con " + str(g.devolver_cant_vertices()) + " vertices y " + str(len(g.devolver_aristas())) + " aristas, tardo: " + str(end - start) + " segundos")