INFINITO = float("inf")


class FloydWarshall(object):
    def __init__(self, grafo):
        self.grafo = grafo
        n = self.grafo.devolver_cant_vertices()
        self.camino = [[INFINITO for i in range(n)] for j in range(n)]
        for i in range(n):
            self.camino[i][i] = 0

    def floydWarshall(self):
        aristas = self.grafo.devolver_aristas_list()
        for a in aristas:
            self.camino[a.id1][a.id2] = a.peso

        vertices = self.grafo.devolver_vertices()
        for k in vertices:
            for j in vertices:
                for i in vertices:
                    nuevo_camino = self.camino[i][k] + self.camino[k][j]
                    if self.camino[i][j] > nuevo_camino:
                        self.camino[i][j] = nuevo_camino
        return self.camino
