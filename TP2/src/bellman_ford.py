INFINITO = float("inf")


class BellmanFord(object):
    def __init__(self, grafo):
        self.grafo = grafo

    def _inicializar_iterador(self):
        """Devuelve un diccionario con la distancia en infinito y otro con los padres seteado en none para cada vertice del grafo """
        distancia = {}
        padre = {}
        for actual in self.grafo.devolver_vertices():
            distancia[actual] = INFINITO
            padre[actual] = None
        return padre, distancia

    def bellmanFord(self, ID):
        """Algoritmo de Floyd Warshall"""
        vertices = self.grafo.devolver_vertices()
        aristas = self.grafo.devolver_aristas()
        padre, distancia = self._inicializar_iterador()
        distancia[ID] = 0 #La distancia a si mismo es 0 
        for i in vertices:
            for u in aristas:
                for v in aristas[u]:
                    w = float(aristas[u][v].peso) 
                    if distancia[u] + w < distancia[v]: #Relajamiento de la arista ,si el nuevo camino es menos costoso que el anterior este se convierte en el nuevo camino
                        distancia[v] = distancia[u] + w
                        padre[v] = u
        return padre, distancia

    def resolver_camino_minimo(self, ID):
        return self.bellmanFord(ID)
