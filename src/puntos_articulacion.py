from parser import Parser
from dfs_iterativo import DFSIterativo
import time

"""Utilizar como python puntos_articulacion.py"""


class PuntosArticulacion(object):

    def __init__(self, g):
        self.g = g

    def get_puntos_articulacion(self):
        """Dado un grafo no dirigido, devuelve los puntos de articulacion"""
        # Inicializo variables
        visitado = {}
        puntos_articulacion = set()
        for u in grafo.devolver_vertices():
            visitado[u] = False

        for v in grafo.devolver_vertices():
            if not visitado[v]:
                # Armo el arbol DFS desde v
                dfs = DFSIterativo(grafo, v, visitado)
                dfs.hacer_dfs()
                puntos_articulacion_v = dfs.get_puntos_articulacion()
                # Como v es raiz del arbol, lo saco para analizarlo por separado
                if v in puntos_articulacion_v:  # Aunque deberia estar incluida siempre
                    puntos_articulacion_v.remove(v)
                self.analizar_raiz(dfs.get_predecesor(), puntos_articulacion_v, v)
                puntos_articulacion.update(puntos_articulacion_v)
        return puntos_articulacion

    def analizar_raiz(self, predecesor, puntos_articulacion, v):
        # Analizo la raiz como puntos de articulacion
        hijos = 0
        # Basta con revisar si los adyacentes a v lo tienen como predecesor o no, no es necesario en todos los vertices
        for u in self.g.adyacentes(v):
            if predecesor[u] == v:
                hijos += 1
        if hijos >= 2:
            puntos_articulacion.add(v)


for i in [0, 1, 2, 3, 4, 5, 6, 7]:
    start = time.time()
    parser = Parser()
    grafo = parser.leer_grafo_no_dirigido("../in/ej2/g" + str(i) + ".txt")
    puntos_articulacion = PuntosArticulacion(grafo).get_puntos_articulacion()
    print "Hay", len(puntos_articulacion), "puntos de articulacion"
    end = time.time()
    print("Con " + str(grafo.devolver_cant_vertices()) + " vertices y " + str(len(grafo.devolver_aristas())) + " aristas, tardo: " + str(end - start) + " segundos")
