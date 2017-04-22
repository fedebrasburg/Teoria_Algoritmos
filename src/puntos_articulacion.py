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
        puntos_artic = set()
        for u in g.devolver_vertices():
            visitado[u] = False

        for v in g.devolver_vertices():
            if not visitado[v]:
                # Armo el arbol DFS desde v
                dfs = DFSIterativo(g, v, visitado)
                dfs.hacer_dfs()
                # Como v es raiz del arbol, lo saco para analizarlo por separado
                puntos_artic_v = dfs.get_puntos_artic()
                if v in puntos_artic_v:  # Aunque deberia estar incluida siempre
                    puntos_artic_v.remove(v)
                self.analizar_raiz(dfs.get_predecesor(), puntos_artic_v, v)
                puntos_artic.update(puntos_artic_v)
        return puntos_artic

    def analizar_raiz(self, predecesor, puntos_artic, v):
        # Analizo la raiz como puntos de articulacion
        hijos = 0
        # Basta con revisar si los adyacentes a v lo tienen como predecesor o no, no es necesario en todos los vertices
        for u in self.g.adyacentes(v):
            if predecesor[u] == v:
                hijos += 1
        if hijos >= 2:
            puntos_artic.add(v)


for i in [0, 7, 1, 2, 3, 4, 5, 6]:
    start = time.time()
    parser = Parser()
    g = parser.leerGrafoNoDirigido("../in/ej2/g"+str(i)+".txt")
    puntos_artic = PuntosArticulacion(g).get_puntos_articulacion()
    print "Hay", len(puntos_artic), "puntos de articulacion"
    end = time.time()
    print("Con " + str(g.devolver_cant_vertices()) + " vertices y " + str(len(g.devolver_aristas())) + " aristas, tardo: " + str(end - start) + " segundos")
