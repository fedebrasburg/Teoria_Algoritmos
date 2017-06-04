INFINITO = float("inf")


class FloydWarshall(object):
    def __init__(self, grafo):
        self.grafo = grafo
        
    def floydWarshall(self):
        """Algoritmo de Floyd Warshall"""
        n = self.grafo.devolver_cant_vertices()
        self.camino = [[INFINITO for i in range(n)] for j in range(n)] #Inicializo todos las distancias de la matriz en infinito
        for i in range(n):
            self.camino[i][i] = 0 #Inicializo las distancias de un nodo a si mismo en 0
        aristas = self.grafo.devolver_aristas_list()
        for a in aristas:
            self.camino[a.id1][a.id2] = float(a.peso) 

        vertices = self.grafo.devolver_vertices() 
        for k in vertices:
            for j in vertices:
                for i in vertices:
                    nuevo_camino = self.camino[i][k] + self.camino[k][j]
                    if self.camino[i][j] > nuevo_camino:
                        self.camino[i][j] = nuevo_camino
        return self.camino

    def resolver_camino_minimo(self):
        return self.floydWarshall()