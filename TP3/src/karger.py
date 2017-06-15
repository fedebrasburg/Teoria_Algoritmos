from creador_grafos import crearGrafoConexo
from random import randint


class Karger(object):
    def __init__(self, n):
        self.grafo = crearGrafoConexo(n, "../out/grafoKarger.txt")
        self.array = [i for i in self.grafo.devolver_cant_vertices]  # Aca se guardaran el set al que pertenezcan

    def contraer(self, id1, id2):
        for destino, arista in self.grafo.devolver_aristas()[id2].items():
            # Obtengo el vertice de la arista que no es id2
            vertice = arista.id2 if arista.id1 == id2 else arista.id1
            # Si la arista a agregar no es una arista entre id1 e id2
            if destino != id1:
                self.grafo.agregar_arista_no_dirigida(id1, vertice)
            # Borro la arista original del grafo
            self.grafo.borrar_arista_no_dirigida(id2, vertice)
        # Borro la arista que va de id1 a id2, ya que antes solo borre la de id2 a id1
        self.grafo.borrar_arista_no_dirigida(id1, id2)
        # Borro el vertice que contraje, que se fusiono con id1
        self.grafo.borrar_vertice(id2)
        # Actualizo el set al que pertenece el vertice id2
        self.array[id2] = id1

    def karger(self):
        if self.grafo.devolver_cant_vertices() == 2:
            return self.array
        aristas = self.grafo.devolver_aristas_list()
        aristaRandom = aristas[randint(0, len(aristas) - 1)]
        # De esta form me aseguro que id1 siempre sea menor que id2
        self.contraer(min(aristaRandom.id1, aristaRandom.id2), max(aristaRandom.id1, aristaRandom.id2))
        self.karger()

k = Karger(100)
k.karger()
