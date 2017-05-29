INFINITO = float("inf")


class BellmanFord(object):
    def __init__(self, grafo):
        self.grafo = grafo

    def _inicializar_iterador(self):
        distancia = {}
        padre = {}
        for actual in self.grafo.devolver_vertices():
            distancia[actual] = INFINITO
            padre[actual] = None
        return padre, distancia

    def bellmanFord(self, ID):
        vertices = self.grafo.devolver_vertices()
        aristas = self.grafo.devolver_aristas()
        padre, distancia = self._inicializar_iterador()
        distancia[ID] = 0
        for i in vertices:
            for u in aristas:
                for v in aristas[u]:
                    w = aristas[u][v].peso
                    if distancia[u] + w < distancia[v]:
                        distancia[v] = distancia[u] + w
                        padre[v] = u
        return padre, distancia
