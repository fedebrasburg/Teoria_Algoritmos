INFINITO = float("inf")  # Truco magico de python none < any int < any string
CERO = 0


class FloydWarshall(object):
    def __init__(self, grafo):
        self.grafo = grafo
        n = grafo.devolver_cant_vertices()
        self.camino = [ [ INFINITO for i in range(n) ] for j in range(n) ]
        for i in range(n):
            self.camino[i][i] = 0

    def floydWarhsall(self):
        aristas = self.grafo.devolver_aristas_list()
        for a in aristas:
            self.camino[a.id1-1][a.id2-1] = a.peso

        vertices = self.grafo.devolver_vertices()
        for k in vertices:
            k = k - 1
            for j in vertices:
                j = j - 1
                for i in vertices:
                    i = i - 1
                    if self.camino[i][j] > self.camino[i][k] + self.camino[k][j]:
                        self.camino[i][j] = self.camino[i][k] + self.camino[k][j]
        return self.camino
