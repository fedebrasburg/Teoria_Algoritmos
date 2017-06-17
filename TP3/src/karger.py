from creador_grafos import crearGrafoConexo
from parser import Parser
from os.path import isfile
from random import randint
from math import log
from grafo import Grafo


class Karger(object):
    def __init__(self, n):
        path = "../out/grafoKarger.txt"
        if isfile(path) and int(open(path).readline()) == n:  # Verifico que el archivo ya creado sea de la misma cantidad de nodos
            p = Parser()
            self.grafo = p.leer_grafo_no_dirigido(path)

            # Borrar
            # self.grafo = Grafo()
            # self.grafo.agregar_vertice(0)
            # self.grafo.agregar_vertice(1)
            # self.grafo.agregar_vertice(2)
            # self.grafo.agregar_vertice(3)
            # self.grafo.agregar_arista_no_dirigida(0, 1)
            # self.grafo.agregar_arista_no_dirigida(1, 2)
            # self.grafo.agregar_arista_no_dirigida(2, 3)
            # self.grafo.agregar_arista_no_dirigida(3, 0)
            # self.grafo.agregar_arista_no_dirigida(0, 2)
        else:
            self.grafo = crearGrafoConexo(n, path)
        self.corte = {i:[i] for i in range(self.grafo.devolver_cant_vertices())}  # Aca se guardara el set al que pertenezcan

    def contraer(self, id1, id2):
        for destino, arista in self.grafo.devolver_aristas()[id2].items():
            # Si la arista a agregar no es una arista entre id1 e id2
            if destino != id1:
                self.grafo.agregar_arista_no_dirigida(id1, destino)
            # Borro la arista original del grafo
            self.grafo.borrar_arista_no_dirigida(id2, destino)
        # Borro el vertice que contraje, que se fusiono con id1
        self.grafo.borrar_vertice(id2)
        # Actualizo el set al que pertenece el vertice id2
        self.corte[id1] += self.corte[id2]
        # Borro la key id2 del diccionario
        self.corte.pop(id2, None)

    def karger(self):
        if self.grafo.devolver_cant_vertices() == 2:
            return self.corte, len(self.grafo.devolver_aristas_list()) / 2
        aristas = self.grafo.devolver_aristas_list()
        aristaRandom = aristas[randint(0, len(aristas) - 1)]
        # De esta forma me aseguro que id1 siempre sea menor que id2
        self.contraer(min(aristaRandom.id1, aristaRandom.id2), max(aristaRandom.id1, aristaRandom.id2))
        return self.karger()

resultCorrecto = []
resultError = []
min_corte = 1
n = 50  # Cantidad de vertices
cant_iteraciones = 1
pruebas_por_iteracion = 1000
combinatorio = float(n*(n-1))/2
# for _ in range(cant_iteraciones):
#     correcto = 0
#     error = 0
#     for _ in range(pruebas_por_iteracion):
#         k = Karger(n)
#         corte, aristas = k.karger()
#         if aristas == min_corte:
#             correcto += 1
#         else:
#             error += 1
#     resultCorrecto.append(correcto)
#     resultError.append(error)
# print "Correcto: " + str(sum(resultCorrecto)/float(cant_iteraciones)/float(pruebas_por_iteracion)*100)
# print "Error: " + str(sum(resultError)/float(cant_iteraciones)/float(pruebas_por_iteracion)*100)
# print "La probabilidad de ser correcto deberia ser mayor a " + str(1/combinatorio)

corte_minimo = []
aristas_minimas = 2*n
for _ in range(int(combinatorio*log(n))):
    k = Karger(n)
    corte, aristas = k.karger()
    if aristas < aristas_minimas:
        aristas_minimas = aristas
        corte_minimo = corte
print "El corte minimo encontrado es con " + str(aristas_minimas)
print "La probabilidad de ser correcto es mayor a " + str(1-(1/float(n)))