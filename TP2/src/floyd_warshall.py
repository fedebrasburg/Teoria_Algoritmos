INFINITO = float("inf")


class FloydWarshall(object):
    def __init__(self, grafo):
        self.grafo = grafo
        n = self.grafo.devolver_cant_vertices()
        self.camino = [[INFINITO for i in range(n)] for j in range(n)]
        for i in range(n):
            self.camino[i][i] = 0

    # Recordar que los ids de vertices comienzan en 1, pero en la matriz es en 0, por eso se resta 1
    def floydWarshall(self):
        aristas = self.grafo.devolver_aristas_list()
        for a in aristas:
            self.camino[a.id1 - 1][a.id2 - 1] = a.peso

        vertices = self.grafo.devolver_vertices()
        for k in vertices:
            k = k - 1
            for j in vertices:
                j = j - 1
                for i in vertices:
                    i = i - 1
                    nuevo_camino = self.camino[i][k] + self.camino[k][j]
                    if self.camino[i][j] > nuevo_camino:
                        self.camino[i][j] = nuevo_camino
        return self.camino
