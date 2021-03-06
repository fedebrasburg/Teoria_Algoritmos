import heapq

INFINITO = float("inf")
CERO = 0


class Dijkstra(object):
    def __init__(self, grafo):
        self.grafo = grafo

    def _inicializar_iterador(self):
        """Inicializa variables del iterador"""
        visitado = {}
        distancia = {}
        padre = {}
        for actual in self.grafo.devolver_vertices():
            visitado[actual] = False
            distancia[actual] = INFINITO
            padre[actual] = None
        return visitado, padre, distancia

    def dijkstra(self, ID):
        """Realiza el algoritmo de Dijkstra, devuelve las distancias y los padres encontrados desde el ID"""
        vertices = self.grafo.devolver_vertices()
        if ID not in vertices:
            return
        heap = []
        visitado, padre, distancia = self._inicializar_iterador()
        distancia[ID] = CERO  # La distancia a si mismo es 0 
        nodo = Nodo(ID, distancia[ID], padre[ID])
        heapq.heappush(heap, nodo)
        while heap:
            nodo = heapq.heappop(heap)
            ID = nodo.ID
            if not visitado[ID]:
                visitado[ID] = True
                padre[ID] = nodo.padre
                distancia[ID] = nodo.distancia
                for ID_ady in self.grafo.adyacentes(ID):
                    nueva_distancia = distancia[ID] + self.grafo.peso_arista(ID, ID_ady)
                    if nueva_distancia < distancia[ID_ady]: #  Relajamiento
                        nodo_nuevo = Nodo(ID_ady, nueva_distancia, ID)
                        heapq.heappush(heap, nodo_nuevo)
        return distancia, padre

    def resolver_camino_minimo(self, ID):
        return self.dijkstra(ID)

class Nodo(object):
    """Clase auxiliar para representar un vertice con toda la informacion pertenciente al algoritmo"""
    def __init__(self, ID, distancia, padre=None):
        self.ID = ID
        self.distancia = distancia
        self.padre = padre

    def __cmp__(self, otro):
        if self.distancia == otro.distancia:
            return 0
        if self.distancia > otro.distancia:
            return 1
        return -1

    def inverse_cmp(self, otro):
        return -self.__cmp__(otro)
